#(1)class attributes// are attributes that are specific to a class not to an instance where to an object to the class
class Person:
    number_of_people=0 #this is a class attribute not a regular attribute as it does not use self-
    #and this attribute does not have access to an instance of the class
    #It is not defined in a method function
    #IT is not specific against instances
    #it is defined for the entire class
    #it is not gonna change from person to person(P1 and p2)
    def __init__(self,name):
    	self.name=name
    	Person.number_of_people+=1 #to keep track of number of people or instances we create for the class
p1=Person("Tim")
print(Person.number_of_people)
p2=Person("Bob") 
print(Person.number_of_people)  

#print(Person.number_of_people)#gives output as it is specific to a class
#we can access number_of_people with class name
#this means we can also change it using the name of the class like below code
#Person.number_of_people = 8
#print(Person.number_of_people)
#print(p1.number_of_people) #python interprets this like this-
#p1 is a person and class person has attribute number_of_people hence print the given or set value
