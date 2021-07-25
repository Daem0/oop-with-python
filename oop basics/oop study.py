class Student:
	def __init__(self,name,age,grade):
		self.name=name
		self.age =age
		self.grade=grade #0-100
	def get_grade(self):
		return self.grade #defining method get_grades to fetch grades from class init method containing parameter grade
class Course:
	def __init__(self,name,max_students):
		self.name=name
		self.max_students=max_students
		self.students=[]#we are free to define attribute students here without adding it to the argument
	def add_student(self,student):#the student here is an instance of student object
	    if len(self.students)<(self.max_students):#if no of students enrolled is less than max number of students needed then 
	    	self.students.append(student)         #add the number of students in argument student to list([]) students(self.students)
	    	return True
	    	return False
	def get_average(self):
	    value = 0
	    for student in self.students:
	    	value+=student.get_grade()

	    return value/len(self.students)	


s1 = Student("robin",19,95)#we add students
s2 = Student("morris",18,80)
s3 = Student("babu",20,90)

course = Course("science",2)
course.add_student(s1) #we call the method add.student() ande we add student  s1 to course
course.add_student(s2)
print(course.students)
#[<__main__.Student object at 0x000002C2E19CB070>, <__main__.Student object at 0x000002C2E19CB460>] this means that we have student object at this particular location
#both students are objects in the list students
print(course.students[0].name)#prints name of the object at the zero index of list students
print(course.get_average())
