#            DONE 100%

class Bikes:
	def __init__(self, description, cost, sale_price, condition, sold=False):
		self.__sold = sold
		self.__condition = condition
		self.__sale_price = sale_price
		self.__cost = cost
		self.__description = description
	
	def updateSale(self, sale):
		if self.__sold:
			return "Action not allowed, Bike has already been sold"
		self.__sale_price = sale
	
	def selled(self, sell):
		self.__sold = True
	
	def desc(self):
		return self.__sold, self.__sale_price, self.__cost, self.__description, self.__condition

bike1 = Bikes()
bike1.desc()