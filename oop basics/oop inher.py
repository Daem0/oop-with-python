class Pet:
	def __init__(self,name,age):
		self.name=name
		self.age =age
	def show(self):
		print(f"Hii i am  {self.name} and i am  {self.age}  years old")
	def speak(self):
	    print(f"I DONT KNOW WHAT TO SAY!!!!!!")	
#NOTE:pet is a general class wheras cat and dog are specific
#class Cat(Pet):this line means that class Cat inherits attributes from main class Pet
#general class has attributes name and age and specific-
#specific class cat and dog have different speak method functions
#here inheritance is used to enter data via inheriting .hence no need-
#to type name and age twicw for cat and dog(see 1 and 2 commented lines)
#cat and dog inherits attributes name and age from general class pet
#TIMESTAMP=enter time input




class Cat(Pet):
	def __init__(self,name,age,color):
		super().__init__(name,age)#super means reference to superclass ie.Pet class for referring attributes name and age so that there is no need to type gain
		self.color=color
	# (1)def __init__(self,name,age):
		#self.name=name
	#	self.age =age
	def speak(self):
		print("MEOOW")
	def show(self):
		print(f"I AM {self.name} AND I AM {self.age} YEARS OLD AND I AM OF {self.color} COLOR")
class Dog(Pet):
	# (2)def __init__(self,name,age):#inhertance can be used so that there is no need to write the attribute definition twice
		#self.name=name
		#self.age =age
	def speak(self):
		print("BARK")
class Fish(Pet):
    pass		
#p=Pet("tim",19)#creating a Pet instance
#p.show()
c=Cat("billi",20,"yellow") #creating a Cat instance
c.show()
#d=Dog("pusi",19) #creating a Dog instance
#d.show()
#d.speak()
#c.speak()
#f = Fish("nemo",9)
#f.speak


