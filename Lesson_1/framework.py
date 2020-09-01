from jinja2 import Template


class Application:
	
	def __init__(self, routes, fronts):
		self.routes = routes
		self.fronts = fronts
	
	def __call__(self, environ, start_response):
		path = environ['PATH_INFO']
		if path in self.routes:
			view = self.routes[path]
		else:
			view = Not_found_404_view()
		request = {}
		# front controllers
		for front in self.fronts:
			front(request)
		# page controllers
		code, body = view(request)
		start_response(code, [('Content-Type', 'text/html', 'charset=utf-8')])
		return body
	
	def render(self, template_name, **kwargs):
		with open(template_name) as f:
			template = Template(f.read())
		template_render = template.render(**kwargs)
		template_render_encode = template_render.encode('UTF-8')
		return template_render_encode


class Not_found_404_view:
	def __call__(self, request):
		content = [b'<p style="font-size: 120px;">404 Page Not Found</p>']
		return '404 WHAT', content
	
	

