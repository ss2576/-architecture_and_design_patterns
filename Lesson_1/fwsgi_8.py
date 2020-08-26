class Index_view:
	def __call__(self):
		return '200 OK', [b'Index']


class Abc_view:
	def __call__(self):
		return '200 OK', [b'ABC']


class Not_found_404_view:
	def __call__(self):
		return '404 WHAT', [b'404 Page Not Found']


class Other:
	def __call__(self):
		return '200 OK', [b'<h4>Other</h4>']


routes = {
	'/': Index_view(),
	'/abc/': Abc_view(),
	'/other/': Other(),
}


class Application:
	
	def __init__(self, routes):
		self.routes = routes
	
	def __call__(self, environ, start_response):
		print('work')
		path = environ['PATH_INFO']
		if path in self.routes:
			view = self.routes[path]
		else:
			view = Not_found_404_view()
		code, body = view()
		start_response(code, [('Content-Type', 'text/html')])
		return body


application = Application(routes)
