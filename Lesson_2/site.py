from framework import Application, Render


class IndexView:
	def __call__(self, request):
		list = [{'name': 'Leo'}, {'name': 'Kate'}]
		content = render('./html/index.html', object_list=list)
		return '200 OK', content


class AbcView:
	def __call__(self, request):
		list = [{'city': 'Moscow'}, {'city': 'Volgograd'}, {'city': 'Orel'}]
		content = render('./html/abc.html', object_list=list)
		return '200 OK', content


class Other:
	def __call__(self, request):
		list = [{'tel': 74523651}, {'tel': 75362159}, {'tel': 789654123}]
		content = render('./html/other.html', object_list=list)
		return '200 OK', content
	
	
class Contacts:
	def __call__(self, request):
		list = [{}]
		content = render('./html/form_contacts.html', object_list=list)
		return '200 OK', content
	
	
class PostInfo:
	def __call__(self, request):
		list = [{}]
		content = render('./html/created_contacts.html', object_list=list)
		return '201 Created ', content


routes = {
	'/': IndexView(),
	'/abc/': AbcView(),
	'/other/': Other(),
	'/contacts/': Contacts(),
}

routes_post = {
	'/abc/': AbcView(),
	'/other/': Other(),
	'/contacts/': PostInfo(),
}


def secret_front(request):
	request['secret'] = 'some secret'


def other_front(request):
	request['key'] = 'key'


fronts = [secret_front, other_front]

application = Application(routes, routes_post, fronts)
render = Render()