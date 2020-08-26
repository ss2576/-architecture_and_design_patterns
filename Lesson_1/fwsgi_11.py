class Index_view:
	def __call__(self, request):
		print(request)
		return '200 OK', 'index.html'



class Abc_view:
	def __call__(self, request):
		print(request)
		return '200 OK', [b'ABC']


class Not_found_404_view:
	def __call__(self, request):
		print(request)
		return '404 WHAT', [b'404 Page Not Found']


class Other:
	def __call__(self, request):
		print(request)
		return '200 OK', [b'<h4>Other</h4>']


routes = {
	'/': Index_view(),
	'/abc/': Abc_view(),
	'/other/': Other(),
}


def secret_front(request):
	request['secret'] = 'some secret'


def other_front(request):
	request['key'] = 'key'


fronts = [secret_front, other_front]


class Application:
	
	def __init__(self, routes, fronts):
		self.routes = routes
		self.fronts = fronts
	
	def __call__(self, environ, start_response):
		print('work')
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
		start_response(code, [('Content-Type', 'text/html')])
		return body


application = Application(routes, fronts)
