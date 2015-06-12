class ParentClass(object):
	def printName(self):
		print("anil")

class ChildClass(ParentClass):
	pass

cobj=ChildClass()
cobj.printName()