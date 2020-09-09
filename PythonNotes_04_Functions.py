# Open Anaconda Prompt
# Run from D:\Program Files\SublimeText\PythonCode>
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# D:\Program Files\SublimeText\PythonCode>python PythonNotes.py 
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart

print("======================================")
print("- Help                                ")
print("======================================")

mylist = [1,2,3]

print(f'For help on commands, go to https://docs.python.org')
print(f'                      go to https://docs.python.org/3/reference/index.html\n')
print(f'Or use the help command (for insert): help(mylist.insert):')
help(mylist.insert)  #can also use shift+tab on Junyper

print("======================================")
print("- Creating a Function                 ")
print("-     def name_of_function(args):     ") #functions snake casing / classes camel casing
print("-         '''                         ") #three ticks - beg
print("-         COMMENT CODE                ") #documentation of the function
print("-         '''                         ") #three ticks - end
print("-         print('Hello + args')       ") #do something 
print("======================================")

def add_two_numbers(num1,num2):	#note functions need to be defined AT TOP
	'''
	Adds two numbers together
	'''
	return num1 + num2			#since you don't define the args, you will need to check data types

num1 = 1
num2 = 2

result = add_two_numbers(num1,num2)		
print(f'{num1} + {num2} = {result}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

def even_check(num):
	'''
	Determines if number if even
	'''
	return num % 2 == 0

number = 2
print(f'{number} is even = {even_check(number)}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

def check_even_list(num_list):
	'''	return true if any number is even in a list '''
	for number in num_list:
		if number % 2 == 0:
			return True
		else:
			pass			#pass lets you continue running thru the loop

	return False

mylist = [1,3,5]
result = check_even_list(mylist)

print(f'Even number in list: {result}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

def check_even_list(num_list):
	'''	return all the even numbers in a list '''
	even_numbers = []

	for number in num_list:
		if number % 2 == 0:
			even_numbers.append(number)
		else:
			pass

	return even_numbers

mylist = [1,3,5,6,8,9,12,13,15,20]
result = check_even_list(mylist)

print(f'Even number in list: {result}')

print("======================================")
print("- Tuple Unpacking                     ")
print("======================================")

stock_prices = [('APPL', 200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
	print (item)

for ticker,price in stock_prices:	#unpacking - you are only printing ticker
	print(ticker)

for ticker,price in stock_prices:	#unpacking - you are only printing prices increases
	print(price+(0.1*price))

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#Find employee of the year, but who has worked the most hours
work_hours = [('Abby',100),('Billie',1400),('Cassie',800)]

def employee_check(work_hours):
	'''checks employee and hours to determine which employee worked the most '''
	current_max = 0
	employee_of_month = ''

	for employee,hours in work_hours:
		if hours > current_max:
			current_max = hours
			employee_of_month = employee
		else:
			pass

	return (employee_of_month,current_max)

print(f'Employee of the month is {employee_check(work_hours)}')

name,hours = employee_check(work_hours) 

print(f'Employee of the month is {name}')

#ERROR Note: If you checked for three values, you may have gotten a
#            ValueError: not enough values to unpack (expected 3, got 2)
#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

print("======================================")
print("- Interactions Between Functions      ")
print("-     Three Cup Monte                 ")
print("======================================")
#Three cup monte - put a ball under three cups and shuffle.  Person picks ball cup

from random import shuffle			#used to shuffle a list / this does not return anything

'''REODERS (SHUFFLES) THE LIST
'''
def shuffle_list(mylist):	
	shuffle(mylist)					
	
	return mylist


'''ALLOWS THE USER TO INPUT WHICH POSITION THE 'O' VALUE WILL BE  
'''
def player_guess():
	guess = ' '

	while guess not in ['0','1','2']:
		guess = input('Pick a number: 0, 1, or 2? ') 

	return int(guess)			#remember input is always a string


'''COMPARES THE USER'S GUESS TO MYLIST TO SEE IF THE USEER GUESSED CORRECTLY 
'''
def check_guess(mylist,guess):
	if mylist[guess] == 'O':
		return 'is CORRECT!!!'
	else:
		return 'is NOT correct'


#INITAL LIST
mylist = [' ','O',' ']			

#SHUFFLE LIST
shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#PRINT REPONSE
print(f'Your guess {guess}, {check_guess(mylist,guess)} | {mylist}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

print("======================================")
print("- *args and **kwargs                  ")
print("======================================")

#*args (Arguements) allows unlimited # of arguements / returns tuple
def myfunc(*args):		#*args can be anything (ie *spam), it's the * that's important, but*args is standard
	print(args)
	return sum(args)

print (f'sum = {myfunc(1,2,3,4,5)}')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#**kwargs (Keyword Arguements) allows umlimited # of keyword arguements / returns dictonary
def myfunc(**kwargs):	
	print(kwargs)

	if 'fruit' in kwargs:
		print ('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print (f'I did not find any fruit')

myfunc(fruit='apple',veggie='lettuce')

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
def myfunc(*args,**kwargs):
	print(args)
	print(kwargs)
	print ('I would like {} {}'.format(args[0],kwargs['food'])) 

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')



#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#return a matching string where every even letter is uppercase and odd lowercase
#    ex birding  = bIrDiNg

def myfunc(word):
    mystring = ""
    count = 0

    for letter in word:
    	count += 1
    	if count % 2 == 0:
    		mystring += letter.upper()
    	else:
    		mystring += letter.lower()

    return mystring

print(f"{myfunc('birding')}")


