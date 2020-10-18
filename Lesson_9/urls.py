from views import Index, CategoryList, CourseList, CreateCourse, CreateUser, CreateCoursePost, CreateCategory, \
	CreateCategoryPost, CreateUserPost, UserList, SelectedUser, SelectedUserPost, AttachUserCourse, RemoveUserCourse,\
	RemoveCourse, RemoveCaregory, RemoveUser
		

routes = {
	'/': Index(),
	'/course-list/': CourseList(),
	'/category-list/': CategoryList(),
	'/user-list/': UserList(),
	'/create-course/': CreateCourse(),
	'/create-category/': CreateCategory(),
	'/create-user/': CreateUser(),
	'/selected_user/': SelectedUser(),
	'/attach-user-course/': AttachUserCourse(),
	'/remove-user-course/': RemoveUserCourse(),
	'/remove-category/': RemoveCaregory(),
	'/remove-course/': RemoveCourse(),
	'/remove-user/': RemoveUser(),
}

routes_post = {
	'/create-course/': CreateCoursePost(),
	'/create-category/': CreateCategoryPost(),
	'/create-user/': CreateUserPost(),
	'/selected_user/': SelectedUserPost(),
}