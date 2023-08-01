#                DONE
import datetime


class Person:
	def __init__(self, name, age, gender):
		self.__name = name.capitalize()
		self.__age = age
		self.__gender = gender

	def getInfo(self):
		return f"The name is: {self.__name}, age : {self.__age}, gender : {self.__gender}"


class Client(Person):
	def __init__(self, name, age, gender, money=0):
		super(Client, self).__init__(name, age, gender)
		self.__money = money
	
	def cashDraw(self):
		add = int(input("How many you add"))
		self.__money += add
		t = datetime.datetime.now().strftime('%A %d %B %Y  %H %M')
		return f"YOU added to your account {add} SR \nin {t}\nyour account now is {self.__money} "
	
	def take(self):
		if self.__money == 0:
			return "Sorry you can't take from your account"
		take = int(input("How many you take"))
		self.__money -= take
		t = datetime.datetime.now().strftime('%A, %-d %B %Y time %-H:%M')
		return f"YOU took to your account {take} SR \nin {t}\nyour account now is {self.__money} "
	
	def getAccount(self):
		return f"the account is {self.__money}"


