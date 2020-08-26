def application(environ, start_response):
	print(type(environ))
	print(environ)
	start_response('200 OK', [('Contetnt-Type', 'text/html')])
	return [b'Hello world from a simple WSGI application!']