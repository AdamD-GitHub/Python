# Open Anaconda Prompt
# Navigate to code directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart


#SPECIAL METHODS (aka Magic or Dunder "double underscores" Methods)
#	Let you use everyday methods with objects, len, print, etc...

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#issue

class Sample():
	
	pass

#main
mysample = Sample()

#len(mysample)  		#you get a type error
print(f'{mysample}')	#Result: <__main__.Sample object at 0x000001AAB299C370>

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#STRINGS AND PRINTING:

class Book():

	def __init__(self,title,author,pages):

		self.title = title
		self.author = author
		self.pages = pages

#main
b = Book('Python rocks','Jose',200)

print(b)			#print asks, what is the string representation of 'b'

#---
print("\n...So write this instead\n")
#---

class Book():

	def __init__(self,title,author,pages):

		self.title = title
		self.author = author
		self.pages = pages

	#STRINGS AND PRINTING:
	def __str__(self):				#string format
		return f"{self.title} by {self.author}"

	#LENGTH:
	def __len__(self):
		return self.pages

	#DELETE an object:
	def __del__(self):
		print ("A book project has been deleted")

#main
b = Book('Python rocks','Jose',200)

print(b)			#it still asks for string representation, but you have a method to format it
print(len(b))
del b
#print(b)			#now you will get an error stating b is not defined

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

class Line:

	def __init__(self,coor1,coor2):
		self.coor1 = coor1			
		self.coor2 = coor2

	def distance(self):

		x1,y1 = self.coor1				#unpack tuples
		x2,y2 = self.coor2

		return ((x2-x1)**2 + (y2-y1)**2)**0.5

	def slope(self):
		
		x1,y1 = self.coor1
		x2,y2 = self.coor2

		return (y2-y1) / (x2-x1)

#main
c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)

print(f"Distance = {myline.distance()} | Slope = {myline.slope()}")

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

class Cylinder():

	pi = 3.14

	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):

		return self.height * self.pi * (self.radius)**2

	def surface_area(self):

		top = self.pi * (self.radius**2)		

		return (2 * top) + (2 * self.pi * self.radius * self.height)

#main
mycyl = Cylinder(2,3)

print(f"Volume = {mycyl.volume()} | Surface Area = {mycyl.surface_area()}")

