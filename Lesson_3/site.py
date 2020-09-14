from framework import Application, Render


class IndexView:
	def __call__(self, request):
		names = [{'name': 'Leo'}, {'name': 'Kate'}]
		data = {
			'title': 'Главная страница',
			'names': names,
		}
		content = render('index.html', object_list=data)
		code = '200 OK'
		return code, content


class AbcView:
	def __call__(self, request):
		citys = [{'city': 'Moscow'}, {'city': 'Volgograd'}, {'city': 'Orel'}]
		data = {
			'title': 'ABC',
			'citys': citys,
		}
		content = render('abc.html', object_list=data)
		code = '200 OK'

		return code, content


class Other:
	def __call__(self, request):
		telephones = [{'tel': 74523651}, {'tel': 75362159}, {'tel': 789654123}]
		data = {
			'title': 'Other',
			'telephones': telephones,
		}
		content = render('other.html', object_list=data)
		code = '200 OK'

		return code, content
	
	
class Contacts:
	def __call__(self, request):
		data = {
			'title': 'Form contacts',
			'request': request,
		}
		content = render('form_contacts.html', object_list=data)
		code = '200 OK'

		return code, content
	
	
class PostInfo:
	def __call__(self, request):
		data = {
			'title': 'Created contacts',
			'request': request,
		}
		content = render('created_contacts.html', object_list=data)
		code = '202 Accepted '

		return code, content


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
