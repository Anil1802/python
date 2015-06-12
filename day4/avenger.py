class Avenger:
	avengersCount=0

	def __init__(self,name,power):
		Avenger.avengersCount +=1
		self.name = name
		self.power = power
	def howmany():
		print("total number of Avengers %d "% avengersCount)

	def getName(self):
		print("Avenger Name : "+self.name+" have power "+self.power)


hulk = Avenger("hulk","Angryness")
print(hulk.name)
print(hulk.power)
print("avengersCount : ", Avenger.avengersCount)

ironMan=Avenger("ironMan","Suite")
print(ironMan.name)
print(ironMan.power)

hulk.getName()
hulk.size="Very Big"

print(hulk.size)

del hulk.power

print(ironMan.name)

x=getattr(hulk,"name")

print(x)

print(setattr(hulk,"name","badahulk"))
print(hulk.name)
print(x)