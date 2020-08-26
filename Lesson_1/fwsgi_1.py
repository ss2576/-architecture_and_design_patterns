def application(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    text = 'Привет Сергей!'
    content = text.encode('UTF-8')
    return content