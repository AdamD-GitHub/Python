# Open Anaconda Prompt
# Navigate to code directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart

'''
SCOPE:
Local: 		
	Names assigned in any way within a function (def or lambda), and not
	declared global in that function.
Enclosing function locals:
	Names in the local scope of any and all enclosing functions (def or lambda), 
	from inner to outer.	
Global:
	Names assigned at the top-level of a module file, or declared global
	in a def within the file.
Built-in:
	Names preassigned in the built-in names module : open, range, Syntac Error...
	ie, if you can use help on it, then it's built in (len, etc)
'''



my_nums = [1,2,3,4,5]
names = ['Andy','Eve','Sally']

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#Local - scope is inside lambda statements

print(f'{list(map(lambda num:num**2,my_nums))}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#Enclosing function locals - scope is inside functions statements

name = 'THIS IS A GLOBAL STRING'

def greet():
	name = 'Sammy'

	def hello():
		print('Hello '+name)	#can't find local/finds enclosing

	hello()

greet()

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#Global - 

name = 'THIS IS A GLOBAL STRING'

def greet():
#	name = 'Sammy'

	def hello():
		print('Hello '+name)	#can't find local/can't find enclosing/finds global

	hello()

greet()

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#Global - 

#GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
 	#ENCLOSING
	name = 'Sammy'

	def hello():
	#LOCAL
		name = 'IM A LOCAL'
		print('Hello '+name)	#finds local

	hello()

greet()

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#GLOBAL
x = 50

def func(x):
	print(f'X is {x}')

	#LOCAL
	x = 200
	print(f'I JUST LOCALLY CHANGED X TO {x}')

func(x)
print(f'X is {x}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#GLOBAL - Changing a GLOBAL inside a function

x = 50

def func():
	global x 	#tells python you want the GLOBAL variable - don't accept as parameter
	print(f'X is {x}')

	#LOCAL
	x = 'NEW VALUE'
	print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

func()
print(f'X is {x}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#GLOBAL - Changing a GLOBAL inside a function (write of above)
#		THIS is the best way to change a GLOBAL variable, take it in a parm and change
#		THIS is MUCH easier to debug!!!

x = 50

def func(x):

	print(f'X is {x}')

	#LOCAL
	x = 'NEW VALUE'
	print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
	
	return x

x = func(x)
print(f'X is {x}')

