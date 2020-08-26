# page controller
def index_view():
	# возвращает тело ответа в виде списка из байт
	return '200 OK', [b'Index']


def abc_view():
	return '200 OK', [b'ABC']


def not_found_404_view():
	return '404 WHAT', [b'404 Not Found']


routes = {
	'/': index_view,
	'/abc/': abc_view,
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
			view = not_found_404_view
		code, body = view()
		start_response(code, [('Content-Type', 'text/html')])
		return body
	
application = Application(routes)

print(application.routes)