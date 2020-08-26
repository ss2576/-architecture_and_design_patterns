# page controller
def index_view(request):
    print(request)
    # возвращаем тело ответа в виде списка из bite
    return '200 OK', [b'Index']


def abc_view(request):
    return '200 OK', [b'ABC']


def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 PAGE Not Found']


class Other:

    def __call__(self, request):
        return '200 OK', [b'<h1>other</h1>']


routes = {
    '/': index_view,
    '/abc/': abc_view,
    '/other/': Other()
}


# Fron controllers
def secret_front(request):
    request['secret'] = 'some secret'


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front]


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        """
            :param environ: словарь данных от сервера
            :param start_response: функция для ответа серверу
            """
        # сначала в функцию start_response передаем код ответа и заголовки
        # print(type(environ))
        # print(environ)
        print('work')
        path = environ['PATH_INFO']
        view = not_found_404_view
        if path in self.routes:
            view = self.routes[path]
        request = {}
        # front controller
        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return body


application = Application(routes, fronts)

# Для запуска можно использовать gunicorn или uwsgi или их аналоги

# gunicorn
# pip install gunicorn
# gunicorn simple_wsgi:application

# uwsgi
# pip install uwsgi
# uwsgi --http :8000 --wsgi-file simple_wsgi.py
