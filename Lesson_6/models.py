from framework.prototypes import PrototypeMixin


class Course(PrototypeMixin):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self,)


class CourseFactory:
    course_class = Course

    @classmethod
    def create(cls, name, category):
        return cls.course_class(name, category)


class TrainingSite:
    # Интерфейс
    def __init__(self):
        self.courses = []
        self.categories = []
        self.users = []
        self.user_types = UserFactory.user_types

    def create_category(self, name, category=None):
        return Category(name, category)

    def find_category_by_id(self, category_id):
        for item in self.categories:
            if item.category_id == category_id:
                return item
        raise Exception(f'Нет категории с category_id = {category_id}')

    def create_course(self, name, category):
        return CourseFactory.create(name, category)

    def get_course(self, name) -> Course:
        for item in self.courses:
            if item.name == name:
                return item
        return None
    
    def create_user(self, name, user_type):
        return UserFactory.create(name, user_type)

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.category_id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []
        self.quantity_of_courses = 0
   
    def course_count(self):
        self.quantity_of_courses = 0
        for elem in self.courses:
            self.quantity_of_courses += 1
            

class User:
    auto_id = 0

    def __init__(self, name, user_type_, sample_discount):
        self.user_id = User.auto_id
        User.auto_id += 1
        self.name = name
        self.user_type = user_type_
        self.sample_discount = sample_discount
        self.discount = self.sample_discount
        self.discount_percent = str(int(self.discount*100)) + '%'
        self.courses = []
        self.quantity_of_courses = 0
        
    def get_course_by_id(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None
    
    def course_remove(self, name):
        if self.courses.count(name) > 0:
            self.courses.remove(name)
        else:
            raise Exception(f'Нет курса с именем  "{name}" ')

    def course_count(self):
        self.quantity_of_courses = 0
        for elem in self.courses:
            self.quantity_of_courses += 1
            
    def discount_course(self):
        if self.quantity_of_courses <= 2:
            self.discount = self.sample_discount
        if self.quantity_of_courses > 2 and self.quantity_of_courses < 5:
            self.discount = 0.05
            self.discount += self.sample_discount
        if self.quantity_of_courses >= 5 and self.quantity_of_courses < 10:
            self.discount = 0.1
            self.discount += self.sample_discount
        if self.quantity_of_courses >= 10 and self.quantity_of_courses < 20:
            self.discount = 0.2
            self.discount += self.sample_discount
        if self.quantity_of_courses >= 20:
            self.discount = 0.4
            self.discount += self.sample_discount
        self.discount_percent = str(int(self.discount * 100)) + '%'


class Teacher(User):
    discount = 0.5
    pass


class Student(User):
    discount = 0.1
    pass


class View(User):
    discount = 0
    pass


class SimpleFactory:
    # Фабричный метод
    def __init__(self, types=None):
        self.types = types or {}


class UserFactory:
    user_types = {
        'Студент': Student,
        'Учитель': Teacher,
        'Для просмотра': View,
    }

    @classmethod
    def create(cls, name, user_type_):
        discount = cls.user_types[user_type_].discount
        return cls.user_types[user_type_](name, user_type_, discount)


site = TrainingSite()


