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
#INHERITANCE
#A way to form new classes from classes that have already been defined
#		reuse code
#       reduce complexity

#BASE CLASS

class Animal():
	
	def __init__(self): 
		print("ANIMAL CREATED")

	def who_am_i(self):
		print("I am animal")

	def eat(self):
		print("BBBBEEEEELLLLCCCCCHHHH!!!!")


class Dog(Animal):		#This is a derived class, derived from Animal

	def __init__(self):
		Animal.__init__(self)
		print("Dog Created")

	def who_am_i(self):
		print("I am a dog")		#This overrides the animal method

	def bark(self):
		print("WOOF!")


#main
my_animal = Animal() 
my_animal.who_am_i()
my_animal.eat()
print("")
mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#POLYMORPHISM
#Polymorphism refers to the way in which different object classes can share the same 
#    method name.  And then those methods can be called from the same place even though 
#    a variety of different objects might be passed in.
#    Basic idea is you have these two separate classes that happen to share the same 
#    method name allowing you to then call those same method names without needing to 
#    worry about the specific class that's being passed in.

#    Both of these share a method name called speak.  

class Dog():
	def __init__(self,name): 

		self.name = name

	def speak(self):
		return self.name + " says woof!"

class Cat():
	def __init__(self,name): 

		self.name = name

	def speak(self):
		return self.name + " says meow!"

def pet_speak(pet):
	print

#main
niko = Dog("Niko")
felix = Cat("Felix")

print(f'{niko.speak()}, {felix.speak()}')

'''
Both niko and felix share the same method speak, but they are different types.  pet_speak doesn't
    know if your going to pass in a dog or cat.  You pass in different objects, but get specific
    object results.
'''
for pet in [niko,felix]:
	print(type(pet))
	print(type(pet.speak()))

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#ABSTRACT CLASSES
#	A class that never expects to be instantiated.  It serves as a base class.
#   It expects you to inherit the Abstract class and override the methods.
#	A good example is an OPEN FILE class for reading files.  You have a function, and you 
#   perform many processes with it.  

class Animal():				#Abstract class

	def __init__(self,name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

	def speak(self):
		return self.name + " says woof!"

class Cat(Animal):

	def speak(self):
		return self.name + " says meow!"

#main
niko = Dog("Niko")
felix = Cat("Felix")

print(f'{niko.speak()}, {felix.speak()}')
