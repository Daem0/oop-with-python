class Person:
	number_of_people= 0




	def __init__(self,name):
		self.name = name
		Person.add_person() #call class method add person to class person and then add

	@classmethod
	def number_of_people_(cls):
	    return cls.number_of_people
	@classmethod
	def add_person(cls):
	    cls.number_of_people+=1    

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())