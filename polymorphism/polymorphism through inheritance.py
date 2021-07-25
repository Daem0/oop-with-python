class Person:
	def __init__(self,name,age):
		self.name = name
		self.age  = age
	def displayData(self):
	    print("in parent class displayData method")
	    print(self.name)
	    print(self.age)
class Employee(Person):
    def __init__(self,name,age,id):
    	#calling constructer of superclass
        super().__init__(name,age)
        self.empId = id	   
    def displayData(self):
        print("in child class displayData method")
        print(self.name)
        print(self.age)
        print(self.empId)

#person class object
Person = Person("john",40)     
Person.displayData()

#employee class object
emp = Employee("john",40,"EE23")
emp.displayData()        	