from framework.main import Application, Render
from urls import routes, routes_post
from views import fronts
from models import site

application = Application(routes, routes_post, fronts)
render = Render()


@application.add_route('/copy-course/')
def copy_course(request):
	request_params = request['request_params']
	name = request_params['name']
	old_course = site.get_course(name)
	if old_course:
		new_name = f'copy_{name}'
		new_course = old_course.clone()
		new_course.name = new_name
		site.courses.append(new_course)
	categories = site.categories
	courses = site.courses
	data = {
		'title': 'Созданы курсы',
		'categories': categories,
		'courses': courses,
	}
	content = render('create_course.html', object_list=data)
	code = '202 Accepted'
	return code, content