class Cars():
	def __init__(self,name,year):
		self.name = name
		self.year = year
		self.price = 1000000

	def info(self):
		return self.name.title()+' '+str(self.year)

	def Price(self):
		print('price of car',self.name ,'is',self.price)

	def gas_tank(self,capacity):
		self.capacity = capacity
		print('Capacity of gas tank of',self.name,'is',self.capacity)

	def update_price(self,new_price):
		if new_price > 100000:
			self.price = new_price
		else:
			print('price cannot be less than 100000')

class Electric(Cars):
	def __init__(self,name,year):
		super().__init__(name,year)
		self.battery = '2 hours'

	def Battery(self):
		print(self.name,'car have',self.battery,'battery life')

	def update_battery(self,new_battery):
		self.battery = new_battery 

	def gas_tank(self,capacity):
		print(self.name,'car does not have gas tank')
 
car1 = Cars('Audi',1999)
print(car1.info())
car1.Price()

car2 = Cars('Alto',2010)
c2 = car2.info()
print(c2)
car2.price = 100000
car2.Price()

car3 = Cars('i10',2018)
print(car3.info())
car3.gas_tank('5kg')
car3.update_price(50000)
car3.Price()

Ecar1 = Electric('tesla',2016)
print(Ecar1.info())
Ecar1.price = 120000
Ecar1.Price()
Ecar1.update_battery('3 hours')
Ecar1.Battery()
Ecar1.gas_tank('3kg')

