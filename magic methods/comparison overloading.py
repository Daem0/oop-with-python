class Person:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def __gt__(self,other):
	    return self.salary>other.salary
p1=Person("robin",8000)
p2=Person("bob",7000)
print(p1.name,"earns more than",p2.name,'-',p1>p2)	    	