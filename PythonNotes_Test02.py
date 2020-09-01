
#Q1: Use for, .split(), and if to create a Statement that will 
#    print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
print(st)
print(f' ')

mylist = st.split()				#break each word in the sentence into list items

for item in mylist:				#loop thru each waor in the list/use .lower() for caps
	if item[0].lower() == 's':	#check the first letter in each word
		print (f'{item}')

print(f'---')
#A1: ---
for word in st.split():
	if word[0].lower() == 's': 
		print(word)

print(f'-----------')
#-----------------------------------------------------------------
#Q2: Use range() to print all the even numbers from 0 to 10.
#A2

for item in range(0,10,2):	
	print(item)

print(f'-----------')

#-----------------------------------------------------------------
#Q3:  List Comprehension to create a list of all numbers between 
#     1 and 50 that are divisible by 3.

#mylist = [item if item%3==0 else '' for item in range(1,51)]
#mylist = [item for item in range(3,51,3)]

mylist = [item for item in range(1,51)]
mylist3 = []

for item in mylist:
	if item%3 == 0:
		mylist3.append(item)
print (mylist3)

print(f'---')
#A3: ---
mylist = [x for x in range(1,51) if x%3 == 0]
print(mylist)

print(f'-----------')

#-----------------------------------------------------------------
#Q4:  Go through the string below and if the length of a word is 
#     even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

mylist = st.split()

for word in mylist:
	count = 0
	for letter in word:
		count += 1
	if count%2 == 0:
		print(f'{word} is even!')

print(f'---')
#A4: ---
for word in st.split():
	if len(word) % 2 == 0:
		print(word+ ' is even!')

print(f'-----------')

#-----------------------------------------------------------------
#Q5:  Write a program that prints the integers from 1 to 100. 
#     But for multiples of three print "Fizz" instead of the number, 
#     and for the multiples of five print "Buzz". For numbers which are 
#     multiples of both three and five print "FizzBuzz".
#A5:

fizz_ct = 3
buzz_ct = 5

for num in range(1,101):
	if num%fizz_ct == 0 and num%buzz_ct == 0:
		print ('FizzBuzz')
	elif num%fizz_ct == 0:
		print ('Fizz')
	elif num%buzz_ct== 0:
		print ('Buzz')
	else:
		print(num)


print(f'-----------')

#-----------------------------------------------------------------
#Q6:  Use List Comprehension to create a list of the first letters 
#     of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

my_word_list = st.split()
my_letter_list = []

for word in my_word_list:
	my_letter_list.append(word[0])
print(my_letter_list)

print(f'---')
#A6: ---
mylist = [word[0] for word in st.split()]
print(mylist)

