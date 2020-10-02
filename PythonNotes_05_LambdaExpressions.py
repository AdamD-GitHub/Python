# Open Anaconda Prompt
# Run from D:\Program Files\SublimeText\PythonCode>
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# D:\Program Files\SublimeText\PythonCode>python PythonNotes.py 
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart

'''
Lambda functions are functions you only reference once and then never again

MAP FUNCTION: 
map(func, *iterables) --> map object
Make an iterator that computes the function using arguments from each of the iterables.
Stops when the shortest iterable is exhausted.

FILTER FUNCTION:

'''
#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#MAP FUNCTION
# Seems like it lets you run multple functions for a given set with out having to 
# code for each item.  

#SQUARE: Takes in a number and returns it's square
def square(num):
		return num**2

#SPLICER: return EVEN for names with even letters or return first letter
def splicer(mystring):		
	if len(mystring)%2 == 0:
		return 'EVEN'
	else:
		return mystring[0]


#MAIN
my_nums = [1,2,3,4,5]
names = ['Andy','Eve','Sally']

#You can either iterate through it or turn it into a list
for item in map(square,my_nums):  
		print(item)
print(f'{list(map(square,my_nums))}') #notice no () on function, because map calls the function

print(f'{list(map(splicer,names))}') #notice no () on function, because map calls the function

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#FILTER FUNCTION
# Returns either True or False

def check_even(num):
		return num%2 == 0


#MAIN
my_nums = [1,2,3,4,5,6]

#You only want to grab even numbers.
#You can either iterate through it or turn it into a list
for n in filter(check_even,my_nums):  
		print(n)
print(f'{list(filter(check_even,my_nums))}') #notice no () on function, because map calls the function

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#STEPS TO TURN A FUNCTION INTO A LAMBDA
#   Functionality you only plan to use 1 time.  It is also known as an anonymous function
#   No name or keyword
#   Only use them if readable

def square1(num):				#STEP1: square function
	result = num**2
	return result

def square2(num):				#STEP2: condensed function
	return num**2

def square3(num): return num**2	#STEP3: one line, bad cooding but close to Lambda 

#lambda num: num**2				#STEP4: No name also no return because it assumes return

square = lambda num: num **2	#You can assign it to square

num1 = 3
num2 = 5
print(f'{square1(num1)}')
print(f'{square2(num1)}')
print(f'{square3(num1)}')
print(f'{square(num1)}')
print(f'{square(num2)}')

#   You use them in conjuction with other functions
print(f'{list(map(lambda num:num**2,my_nums))}')		#square values
print(f'{list(filter(lambda num:num%2 == 0,my_nums))}')	#get even numbers
print(f'{list(map(lambda name:name[0],names))}')		#get first letter
print(f'{list(map(lambda x:x[::-1],names))}')			#reverse name spellings

