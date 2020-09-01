from framework import Application


class Index_view:
	def __call__(self, request):
		list = [{'name': 'Leo'}, {'name': 'Kate'}]
		content = application.render('./html/index.html', object_list=list)
		return '200 OK', content


class Abc_view:
	def __call__(self, request):
		list = [{'city': 'Moscow'}, {'city': 'Volgograd'}, {'city': 'Orel'}]
		content = application.render('./html/abc.html', object_list=list)
		return '200 OK', content


class Other:
	def __call__(self, request):
		list = [{'tel': 74523651}, {'tel': 75362159}, {'tel': 789654123}]
		content = application.render('./html/other.html', object_list=list)
		return '200 OK', content


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

application = Application(routes, fronts)



