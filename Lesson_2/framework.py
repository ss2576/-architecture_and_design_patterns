from jinja2 import Template
from pprint import pformat


class Application:
	
	def __init__(self, routes, routes_post, fronts):
		self.routes = routes
		self.routes_post = routes_post
		self.fronts = fronts
	def __call__(self, environ, start_response):
		print('ENVIRON')
		print(environ)
		method = environ['REQUEST_METHOD']
		path = environ['PATH_INFO']
		request = {}
		if method == 'GET':
			if path in self.routes:
				view = self.routes[path]
			else:
				view = NotFound404View()
		elif method == 'POST':
			# получаем длину тела
			content_length_data = environ.get('CONTENT_LENGTH')
			print('CONTENT_LENGTH')
			print(content_length_data)
			# приводим к int
			content_length = int(content_length_data) if content_length_data else 0
			# считываем данные если они есть
			data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
			print('wsgi.input')
			print(data)
			view = self.routes_post[path]
		for front in self.fronts:
			front(request)
		code, body = view(request)
		start_response(code, [('Content-Type', 'text/html', 'charset=utf-8')])
		return body
	

class NotFound404View:
	
	def __call__(self, request):
		content = [b'<p style="font-size: 120px;">404 Page Not Found</p>']
		return '404 WHAT', content
	
	
class Render:
	
	def __call__(self, template_name, **kwargs):
		with open(template_name) as f:
			template = Template(f.read())
		template_render = template.render(**kwargs)
		template_render_encode = template_render.encode('UTF-8')
		return template_render_encode
	



