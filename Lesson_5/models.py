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


class Category:
    # реестр?
    auto_id = 0

    def __init__(self, name, category):
        self.category_id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []
   
    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


site = TrainingSite()