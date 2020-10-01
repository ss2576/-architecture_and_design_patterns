from framework.main import Render
from models import site
from logging_mod import Logger, debug

logger = Logger('main')


class IndexView:
	def __call__(self, request):
		logger.log('Главная страница')
		data = {
			'title': 'Главная страница',
		}
		content = render('index.html', object_list=data)
		code = '200 OK'
		return code, content


class CreateCourse:
	def __call__(self, request):
		logger.log('Создание курсов')
		categories = site.categories
		data = {
			'title': 'Создание курсов',
			'categories': categories,
			
		}
		content = render('create_course.html', object_list=data)
		code = '200 OK'
		return code, content


class CreateCategory:
	def __call__(self, request):
		logger.log('Создание категорий курсов')
		categories = site.categories
		data = {
			'title': 'Создание категорий курсов',
			'categories': categories,
		}
		content = render('create_category.html', object_list=data)
		code = '200 OK'
		return code, content


class CreateCategoryPost:
	@debug
	def __call__(self, request):
		name = request['name']
		category = None
		new_category = site.create_category(name, category)
		site.categories.append(new_category)
		categories = site.categories
		data = {
			'title': 'Созданы категории',
			'new_category': new_category,
			'categories': categories,
		}
		content = render('create_category.html', object_list=data)
		code = '202 Accepted'
		return code, content


class CreateCoursePost:
	@debug
	def __call__(self, request):
		name = request['name']
		category_id = request['category_id']
		category = None
		if category_id:
			category = site.find_category_by_id(int(category_id))
			course = site.create_course(name, category)
			site.courses.append(course)
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
	
	
class CategoryList:
	def __call__(self, request):
		categories = site.categories
		data = {
			'title': 'Список категорий',
			'categories': categories,
		}
		content = render('category_list.html', object_list=data)
		code = '202 Accepted'
		return code, content
	
	
class CourseList:
	def __call__(self, request):
		courses = site.courses
		data = {
			'title': 'Список курсов',
			'courses': courses,
		}
		content = render('course_list.html', object_list=data)
		code = '202 Accepted'
		return code, content



def secret_front(request):
	request['secret'] = 'some secret'


def other_front(request):
	request['key'] = 'key'


fronts = [secret_front, other_front]

render = Render()
