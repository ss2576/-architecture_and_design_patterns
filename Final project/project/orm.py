from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
import copy


base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=False)


class CategoryBase(base):
	__tablename__ = 'category'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	datetime = Column(DateTime(timezone=False), server_default=func.now())
	
	@staticmethod
	def create_object(object):
		session.add(object)
		session.commit()
		
	@staticmethod
	def delete_object(object):
		courses = session.query(CourseBase).filter_by(category_id=object)
		for elem in courses:
			session.query(SiteUsersBase).filter_by(course_id=elem.id).delete()
		session.query(CourseBase).filter_by(category_id=object).delete()
		session.query(CategoryBase).filter_by(id=object).delete()
		session.commit()


class CourseBase(base):
	__tablename__ = 'course'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'))
	datetime = Column(DateTime(timezone=False), server_default=func.now())
	
	@staticmethod
	def create_object(object):
		session.add(object)
		session.commit()
	
	def clone(self):
		"""Clone a registered object and update inner attributes dictionary"""

		return copy.deepcopy(self)
	
	@staticmethod
	def delete_object(object):
		session.query(SiteUsersBase).filter_by(course_id=object).delete()
		session.query(CourseBase).filter_by(id=object).delete()
		session.commit()


class SiteUsersBase(base):
	__tablename__ = 'site'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	course_id = Column(Integer, ForeignKey('course.id', ondelete='CASCADE'))
	user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
	datetime = Column(DateTime(timezone=False), server_default=func.now())
	
	@staticmethod
	def create_object(object):
		session.add(object)
		session.commit()

	@staticmethod
	def delete_object(object):
		session.query(SiteUsersBase).filter_by(id=object).delete()
		session.commit()

	@staticmethod
	def course_count(user):
		personal_courses = session.query(SiteUsersBase).filter_by(user_id=user.id)

		return personal_courses


class UserBase(base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	user_type = Column(String)
	sample_discount = Column(Integer)
	variable_discount = Column(Integer)
	discount_percent = Column(String)
	quantity_of_courses = Column(Integer)
	datetime = Column(DateTime(timezone=False), server_default=func.now())
	
	@staticmethod
	def create_object(object):
		session.add(object)
		session.commit()
	
	@staticmethod
	def update_object(object):
		session.query(UserBase).filter_by(id=object.id).update({'variable_discount': object.variable_discount})
		session.query(UserBase).filter_by(id=object.id).update({'discount_percent': object.discount_percent})
		session.query(UserBase).filter_by(id=object.id).update({'quantity_of_courses': object.quantity_of_courses})
		session.commit()
	
	@staticmethod
	def delete_object(object):
		session.query(SiteUsersBase).filter_by(user_id=object).delete()
		session.query(UserBase).filter_by(id=object).delete()
		session.commit()
		
	@staticmethod
	def get_quantity_of_courses(user_id):
		query = session.query(UserBase).filter_by(id=user_id)
		for elem in query:
			if elem.id == user_id:
				user = elem
		if user.quantity_of_courses == None:
			quantity_of_courses = 0
		else:
			quantity_of_courses = user.quantity_of_courses

		return quantity_of_courses


base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
