# Open Anaconda Prompt
# Navigate to code directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart


#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#BASIC CLASS STRUCTURE
#create a base class called Dog with attributes.  Add an initialiation method.  
#self - Remember to use 'self' in the init method which connects the instance of the 
#       method to itself.  It represents the instance.  Most OO languages hide this, but 
#       Python requires it.  Technically the name could be anything, but the standard is
#       to call it self.

class Dog():
	def __init__(self,breed,name,spots): 	#initialization method

		self.breed = breed
		self.name = name
		self.spots = spots					#t/f 

#main
my_dog = Dog('Chihuahua','Rover',True) 		#creates instance of class

print(f'My dog is a {my_dog.breed}, {my_dog.name}, {my_dog.spots}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#CLASS OBJECT ATTRIBUTE
#These go at the beginning of the class.  They will be the same for ANY INSTANCE of a class.

#CLASS OBJECT ATTRIBUTE
species = 'mammal'

class Dog():
	def __init__(self,breed,name,spots): 	#initialization method

		self.breed = breed
		self.name = name
		self.spots = spots					#t/f 

#main
my_dog = Dog('Chihuahua','Rover',True) 		#creates instance of class

print(f'My dog is a {species}, {my_dog.breed}, {my_dog.name}, {my_dog.spots}')


#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#WORKING WITH METHODS
#    ie, functions inside of a class
#    NOTICE: ATTRIBUTE gets do not have (), whereas METHOD gets do have ()

class Dog():

	#CLASS OBJECT ATTRIBUTE
	species = 'mammal'

	def __init__(self,breed,name): 	#initialization method

		self.breed = breed
		self.name = name

	#METHODS
	def bark1(self):
		print(f"WOOF! My name is {self.name}")	#It can reference attributes

	def bark2(self,num):
		print(f"WOOF! My name is {self.name} and num is, {num}")


#main
my_dog = Dog('Chihuahua','Rover') 		#creates instance of class

my_dog.bark1()
my_dog.bark2(2)
print(f'My dog is a {my_dog.species}, {my_dog.breed}, {my_dog.name}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#WORKING WITH METHODS

class Circle():
	
	#CLASS OBJECT ATTRIBUTE
	pi = 3.14

	def __init__(self,radius=1): 	#radius has default parameter

		self.radius = radius
		self.area = radius*radius*Circle.pi*2	#Circle.pi = self.pi, Circle more common

	#METHODS
	def get_circumference(self):
		return self.radius * self.pi * 2

#main
my_circle = Circle() 		#creates instance of class
my_circle2 = Circle(30)

print(f'Pi = {my_circle.pi}')
print(f'Radius = {my_circle.radius}')
print(f'Area = {my_circle.area}')
print(f'Circumference = {my_circle.get_circumference()}')
print(f'Pi = {my_circle2.pi}')
print(f'Radius = {my_circle2.radius}')
print(f'Area = {my_circle2.area}')
print(f'Circumference = {my_circle2.get_circumference()}')
