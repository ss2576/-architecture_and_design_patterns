from views import IndexView, CategoryList, CourseList, CreateCourse, \
					CreateCoursePost, CreateCategory, CreateCategoryPost


routes = {
	'/': IndexView(),
	'/course-list/': CourseList(),
	'/category-list/': CategoryList(),
	'/create-course/': CreateCourse(),
	'/create-category/': CreateCategory(),
}

routes_post = {
	'/create-course/': CreateCoursePost(),
	'/create-category/': CreateCategoryPost(),
}