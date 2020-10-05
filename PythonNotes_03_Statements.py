# Open Anaconda Prompt
# Navigate to code directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart
from random import shuffle
from random import randint


print("======================================")
print("- if / elif / else")
print("-    Uses spaces and colons")
print("-    elif = else if")
print("======================================")
if True:
	print(f"It's true")
else:
	print(f"It's false")
print("")

loc = 'Auto Shop'
if loc == 'Auto Shop':
	print(f"Cars are cool")
elif loc == 'Bank':
	print(f"Money is cool")
elif loc == 'Store':
	print(f"Shopping in the store")
else:
	print(f"error")
print("")

print("======================================")
print("- for loops")
print("-   * Syntax: ")
print("-   * my_iterable = [1,2,3]")
print("-   * for item_name in my_iterable:") #print every item_name in my_iterable
print("-   *    print(item_name)")
print("======================================")
mylist = [1,2,3,4,5,6,7,8,9,10]
#print 1-10
for i in mylist: 
	print(f"{i}") 

print("")
#print even numbers and if odd, note odd
for i in mylist:
	if i % 2 == 0:
		print(f"{i}")
	else:
		print(f"Odd number: {i}")

print("")
#print the sum of mylist
list_sum = 0
for i in mylist:
	list_sum = list_sum + i

print(f"{list_sum}")

print("")
#vertically print mystring
mystring = 'hello world'
for i in mystring:
	print(f"{i}")

print("")
#print the word cool! for every charater in mystring
mystring = 'hello world'
for _ in mystring: #'_' is common practice when you don't need variable.
	print(f"Cool!")

print("")
#using tuples --------------------------------------------------
tup = (1,2,3)
for item in tup:
	print(item)

print("")
#tuple unpacking -----------------------------------------------
mylist = [(1,2),(3,4),(5,6),(7,8)]
len(mylist)
for item in mylist: #tuple unpacking returns the tuples in a list
	print(item)
print("---")
for a,b in mylist: #same as using parens --> for (a,b) in mylist ,but more common with none
	print(a)
	print(b)
print("-")
for a,b in mylist: #print only the first item of each tuple
	print(a)
print("-")
mylist = [(1,2,3,4),(5,6,7,8)]
for item in mylist: #tuple unpacking returns the tuples in a list
	print(item)
print("-")
for a,b,c,d in mylist: #need to define tuple structure - 4 in a tuple (a,b,c,d)
	print(b)
print("---")

print("")
#using dictonaries --------------------------------------------
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
	print(item) #by default you only iterate thru keys
print("-")
for item in d.items():
	print(item) #to get back the diconary pairs, use .items()
print("-")
for key,value in d.items():
	print(value) #to only get the values, use .items() and define the structure
	             #   this piggy-backs on tuple unpacking
print("-")
for value in d.values(): #or to only get the values, use .values()
	print(value)	   
print("---")

print("")
print("======================================")
print("- while loops")
print("-   * Syntax: ")
print("-   * while boolean_condition")
print("-   *     do something       ")
print("-   * else                   ")
print("-   *     do something else  ")
print("-                            ")
print("-   KEYWORDS:                ")
print("-      break: Breaks out of the current closest enclosing loop ")
print("-      continue: Goes to the top of the closest enclosing loop ")
print("-      pass: Does nothing at all")
print("-                            ")
print("-   Junyper to stop infinate loop - Kernel - Interrupt")
print("-                              or - Kernel - Restart  ")
print("-   Anaconda Prompt to stop infinate loop - cntl+pause/break ")
print("======================================")
x = 0
while x < 5:
	print(f'The current value of x is {x}')
	x +=1 #aka x = x + 1
else:
	print(f'X is not less than 5')

#pass  -------------------------------------------------------
x = [1,2,3]
for item in x: #if nothing else is after this you get an error
	#comment
	pass #pass is great for a coding placeholder.  Needed because Python uses spaces
print(f'end of my script')

print("---")

#continue  ---------------------------------------------------
mystring ='Sammy'
for letter in mystring:
	if letter == 'a':
		continue
	print(letter)

print("---")

#break  ------------------------------------------------------
mystring ='Sammy'
for letter in mystring:
	if letter == 'a':
		break #great for while statements
	print(letter)
print("")
x = 0
while x < 5:
	if x == 2:
		break
	print(x)
	x +=1

print("---")

print("")
print("======================================")
print("- Useful Operations                           ")
print("-   range (start,stop,step)                   ")
print("-      also range is more efficient than having a list stored in memory")
print("-   enumerate                                 ")
print("-      returns index counter and the element object")
print("-      ie you can do index counting in the form of tuples")
print("-   zip                                       ")
print("-      merges lists into tuples               ")
print("-      only merges the shortest lists         ")
print("-   in                                        ")
print("-      check if object is in a list           ")
print("-   min/max                                   ")
print("-      check min/max                          ")
print("-   random                                    ")
print("-      used to randize a list                 ")
print("-   input                                     ")
print("-      used to input values                   ")
print("-      ALWAYS inputs as a string, so casting may be needed ")
print("======================================")


#range  ------------------------------------------------------
#before we would have to make a list 0-10, instead we could use range
for num in range(10): #stop required
	print(num)
print("")
for num in range(5,10): #start,stop
	print(num)
print("")
for num in range(0,10,2): #start,stop,step
	print(num)	
print("")
print(f"{list(range(0,11,2))}") #to print the range, you will need to cast it to a list

print("---")
#enumerate  --------------------------------------------------
#we want to know what index we are at in a for loop
index_count = 0
for letter in 'abcde':
	print(f'At index {index_count} the letter is {letter}')
	index_count += 1

print("")

index_count = 0
word = 'abcde'

for letter in word:
	print(f'{word[index_count]}')
	index_count += 1
#with enumerate, you get this back in tuples
for item in enumerate(word):
	print(item)
for index,letter in enumerate(word):
	print(index)
	print(letter)
	print('\n')

print("---")
#zip ---------------------------------------------------------
mylist1 = [1,2,3,4,5,6] #note 4,5,6 will NOT be included because the other two list only have 3 values
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
	print(item)
for a,b,c in zip(mylist1,mylist2,mylist3): #unpacking the tuple - prints out letters
	print(b)

print("---")
#in ----------------------------------------------------------
if 'x' in [1,2,3]:
	print('true')
else:
	print('false')
print("")
if 'x' in ['x','y','z']:
	print('true')
else:
	print('false')
print("")

d = {'mykey':345} #great for checking values in dictonaries

if 'mykey' in d.keys(): 
	print('true')
else:
	print('false')

if 345 in d.values(): 
	print('true')
else:
	print('false')

if 345 in d.keys(): 
	print('true')
else:
	print('false')


print("---")
#min/max -----------------------------------------------------
mylist = [10,100,30,40,50]

print(f'min = {min(mylist)}')
print(f'max = {max(mylist)}')

print("---")
#random -----------------------------------------------------
mylist = [1,2,3,4,5,6,7,8,9]

print(f'shuffled list = {shuffle(mylist)}') #shuffle doesn't return anything, so displays none

print(f'random number = {randint(0,100)}')


print("---")
#input ------------------------------------------------------
#result = input('What is your name? ') 
#print(f'Name = {result} / Type = {type(result)}')

#result = int(input('What is your name? ')) #input ALWAYS accepts everything as a string
#print(f'Name = {result} / Type = {type(result)}')

print("---")

print("")
print("======================================")
print("- List Comprehensions                         ")
print("-    Used to short hand iteration code inside list brackets ")
print("-    You can put if/else and nested loops, but readability may suffer ")
print("======================================")

mystring = 'hello'

mylist = []
for letter in mystring:
	mylist.append(letter)
print(f'mylist = {mylist}')

print("")

mystring = 'goodbye'

mylist =[letter for letter in mystring] #this replaces the iteration statements
print(f'mylist = {mylist}')

print("")
mylist = [num**2 for num in range(0,11)] #squaring a list
print(f'mylist = {mylist}')

print("")
mylist = [x**2 for x in range(0,11) if x%2==0] #adding a condition - squares only the even numbers
print(f'mylist = {mylist}')

print("")
#new way
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(f'Celcuis {celcius} = Farenheit {fahrenheit}')
#old way - same as above
fahrenheit = []
for temp in celcius:
	fahrenheit.append(((9/5)*temp + 32))
print(f'Celcuis {celcius} = Farenheit {fahrenheit}')
