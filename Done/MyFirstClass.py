from abc import ABC, abstractmethod


class Person(ABC):
	"""This Class  is the perants class for my humanity classes in my company"""

	def __init__(self, name: str, age: int, gender : str):
		self.__name = name
		self.__age = age
		self.__gender = gender

	@abstractmethod
	def person_info(self):
		print("The name is : ", self.__name)
		print("the age is : ", self.__age)
		print("The gender is : ", self.__gender)
#		print("----------------------")
	

	@abstractmethod
	def change_the_name(self, new_name: str):
	#   self.__name = new_name
	    pass

	@abstractmethod
	def change_gender(self, num):
		pass
	#	self.__salary = num

	@abstractmethod
	def change_age(self, age: int):
	    pass
	
	
	
"""---------------------------------------"""


class Student(Person):


	def __int__(self, name: str, age: int, gender : str, major : str):
		super().__init__(name, age, gender)
		self.__major = major
		
	def person_info(self):
		super().person_info()
		print("The major is : ", self.__major)
		print("----------------------")
		
	def change_the_name(self, new_name: str):
		self.__name = new_name
		
	def change_gender(self, new_gender):
		self.__gender = new_gender
		
	def change_age(self, new_age: int):
		self.__age = new_age
		


"""----------------------------------------"""



class Employee(Person):
	
	
	def __init__(self, name: str, age: int, gender : str, salary : int , is_married : bool):
		super().__init__(name, age, gender)
		self.__salary = salary
		self.__is_maried = is_married
	
#	def person_info(self):
#		super().__init__()
#		self.__salary = salary
	
	def person_info(self):
		super().person_info()
		print("The salary is : ", self.__salary)
		print("----------------------")
	
	def change_the_name(self, new_name: str):
		self.__name = new_name
	
	def change_gender(self, new_gender):
		self.__gender = new_gender
	
	def change_age(self, new_age: int):
		self.__age = new_age
	