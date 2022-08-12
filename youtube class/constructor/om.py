class Students:
	def __init__(self,a,b,c):
		self.name=a
		self.rollno=b
		self.marks=c
	def take(self):
		print("it is my name:",self.name)
		print("it is my marks:",self.marks,"marks,fail")
s=Students( "kiran",101,34)
print(s.name)
print(s.rollno)
print(s.marks)
s.take();