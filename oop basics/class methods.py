class Person:
    number_of_people=0 
    GRAVITY = -9.8


    
    def __init__(self,name):
        self.name=name
        Person.add_person() # calls the class method



    @classmethod#this is a decorator    
    def number_of_people_(cls): #this method definned does not act/is not specific to an instance
        return cls.number_of_people() #this is called upoun the class itself
#this method just acts on the class not on the instance



    @classmethod
    def add_person(cls):
        cls.number_of_people+=1



p1=Person("Tim") #instance1
#print(Person.number_of_people)
p2=Person("Bob") #instance2
#print(Person.number_of_people)
print(
