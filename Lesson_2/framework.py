from jinja2 import Template
from urllib.parse import unquote_plus



class Application:
	
	def __init__(self, routes, routes_post, fronts):
		self.routes = routes
		self.routes_post = routes_post
		self.fronts = fronts
	def __call__(self, environ, start_response):
		method = environ['REQUEST_METHOD']
		path = environ['PATH_INFO']
		request = {}
		if method == 'GET':
			if path in self.routes:
				view = self.routes[path]
			else:
				view = NotFound404View()
		elif method == 'POST':
			""" смотрим, есть ли данные в теле ENVIRON (CONTENT_LENGTH должен быть > 0) """
			post_method = PostMethod()
			input_encode_data = post_method(environ)
			""" получаем декодированные данные с помощью класса WsgiInputDataDecode """
			wsgi_input_data_decode = WsgiInputDataDecode()
			input_data = wsgi_input_data_decode(input_encode_data)
			""" получаем словарь из input_data с помощью класса ParseInputData """
			parse_input_data = ParseInputData()
			request = parse_input_data(input_data)
			view = self.routes_post[path]
		# пока не придумал, в чём задействовать front
		# for front in self.fronts:
		# 	front(request)
		code, body = view(request)
		start_response(code, [('Content-Type', 'text/html')])

		return body
	

class NotFound404View:
	
	def __call__(self, request):
		content = [b'<p style="font-size: 120px;">404 Page Not Found</p>']
		return '404 WHAT', content
	
	
class Render:
	"""
	# вставляет данные в страницу HTML и кодирует данные с помощью encode('UTF-8')
	"""
	def __call__(self, template_name, **kwargs):
		with open(template_name) as f:
			template = Template(f.read())
		template_render = template.render(**kwargs)
		template_render_encode = template_render.encode('UTF-8')
		
		return template_render_encode


class PostMethod:
	"""
	# смотрим, есть ли данные в теле ENVIRON (CONTENT_LENGTH должен быть > 0)
	# возвращает данные в байтовом представлении
	"""
	def __call__(self, environ):
		content_length_data = environ.get('CONTENT_LENGTH')
		content_length = int(content_length_data) if content_length_data else 0
		input_encode_data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
		
		return input_encode_data


class WsgiInputDataDecode:
	"""
	# получаем словарь из данных полученных из POST запроса с помощью parse_qs
	"""
	def __call__(self, input_encode_data: bytes) -> dict:
		if input_encode_data:
			input_decode_data = unquote_plus(input_encode_data.decode('UTF-8'))
			
		return input_decode_data


class ParseInputData():
	""" преобразуем декодированные данные в словарь dict_data """
	def __call__(self, input_data):
		dict_data = {}
		param = input_data.split('&')
		for item in param:
			k, v = item.split('=')
			dict_data[k] = v
			
		return dict_data