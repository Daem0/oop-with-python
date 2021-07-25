class Mul:
	def __init__(self,x):
		self.x=x
	def __mul__(self,other):
	   return self.x*other.x
m1=Mul(2)
m2=Mul(3)
print(m1*m2)	   	