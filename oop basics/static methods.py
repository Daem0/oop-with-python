#STATIC METHODS: THEY ARE USED FOR ORGANISING FUNCTIONS IN A CLASS
#static methods does not change
#they do not have acces to an instance just like class methods
#no need to put self or cls because there is no need to access anything as mentioned above
class Math:
	@staticmethod
	def add5(x):
		return x+5
	@staticmethod
	def add10(x):
		return x+10
	@staticmethod
	def pr():    #pr()means just print.it is a print function
		print("run")
print(Math.add5(6))
print(Math.add10(8))
print(Math.pr())