class Student:
	def __init__(self, name, age, iden):  # This is Attributes for the class
		self.name = name.capitalize()  # Public varible
		self._age = age  #
		self.__id = iden

	def nameGet(self):  # This is a methods in class, out the class called function inside class called method
		return f"the name is : {self.name}"

	@property
	def age(self):
		return self._age


# class dad:
# 	def __init__(self, name, age, id, grades):
# 		self.id = id
# 		self.name = name
# 		self.age = age
# 		self.grades = grades
#
#
# 	def d(self):
# 		return self.__dir__()
#


std1 = Student("ahmed", 23, "xx00")
print(std1.nameGet())
print("-----------")
std1.name = "Ali"
print(std1.name)
print("-----------")
std1._age = 5000
print(std1.age)
print("-------------")
std1.__id = 20
print(std1.__id)
