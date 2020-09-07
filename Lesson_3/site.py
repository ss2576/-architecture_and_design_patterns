from framework import Application, Render


class IndexView:
	def __call__(self, request):
		data_text = [{'name': 'Leo'}, {'name': 'Kate'}]
		list = {
			'data': data_text,
			'title': 'Index',
		}
		content = render('index.html', object_list=list)
		code = '200 OK'
		
		return code, content


class AbcView:
	def __call__(self, request):
		data_text = [{'city': 'Moscow'}, {'city': 'Volgograd'}, {'city': 'Orel'}]
		list = {
			'data': data_text,
			'title': 'ABC',
		}
		content = render('abc.html', object_list=list)
		code = '200 OK'

		return code, content


class Other:
	def __call__(self, request):
		data_text = [{'tel': 74523651}, {'tel': 75362159}, {'tel': 789654123}]
		list = {
			'data': data_text,
			'title': 'Other',
		}
		content = render('other.html', object_list=list)
		code = '200 OK'

		return code, content
	
	
class Contacts:
	def __call__(self, request):
		list = dict(request)
		list['title'] = 'Form contacts'
		content = render('form_contacts.html', object_list=list)
		code = '200 OK'

		return code, content
	
	
class PostInfo:
	def __call__(self, request):
		list = request
		list['title'] = 'Created contacts'
		content = render('created_contacts.html', object_list=list)
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
