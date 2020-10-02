
#Q1: SPHERE VOLUME: Write a function that computes the volume of a sphere
# 	 given it's raduis 
#A1
def vol(rad):

    return (4/3)*(3.14)*(rad**3)

#MAIN
radius = 2

print(f"Volume = {vol(radius)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q2: NUMBER RANGE: Write a function that checks whether a number is in a 
#    given range (inclusive of high and low)
#A2

def ran_check(num,low,high):

	return num in range(low,high+1)	#rem:range does not include the high num.

def ran_check2(num,low,high):

	if num in range(low,high+1):
		print(f"{num} is in the range between {numl} and {numh}")
	else:
		print(f"{num} is NOT in the range between {numl} and {numh}")

#MAIN
num  = 5
numl = 2
numh = 7
print(f"{num} is within the range t/f --> {ran_check(num,numl,numh)}")

ran_check2(num,numl,numh)


#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q3: UPPER AND LOWER: Write a function that accepts a string and calculates
#    the number of upper and lower case letters.  
#A3

def up_low(str1):
	case_results = [sum(map(str.isupper,str1)),sum(map(str.islower,str1))]
	return case_results
	
#MAIN
str1 = "Hello Mr. Rogers, how are you this fine Tuesday?"
case_results = up_low(str1)

print(f"Original String: {str1}")
print(f"No. of Upper case characters : {case_results[0]}")
print(f"No. of Lower case characters : {case_results[1]}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q4: UNIQUE LIST: Write a function that takes a list and returns a new list
#    with unique elements of the first list.
#A4

def unique_list(list1):

	return list(set(list1))	#cast the list to a set then return new list

#MAIN
list1 = [1,1,1,1,2,2,3,3,3,3,3,4,5]

print(f"{list1} --> {unique_list(list1)}")


#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q5: MULTIPLY LIST: Write a function to multiply all the numbers in a list
#A5

def multiply(list1):
	total = 1

	for num in list1:
		total *= num		

	return total

#MAIN
list1 = [1,2,3,-4]

print(f"{list1} --> {multiply(list1)}")

#MAIN

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q6: PALINDROME: Write a function that checks whether a word ot phrase is a 
#    palindrome or not.
#A6

def palindrome(s):

	return s.replace(" ","") == s[::-1].replace(" ","")	#::-1 most popular reverse technique
'''
	if s.replace(" ","") == s[::-1].replace(" ",""):	#replaces spaces in sentence
		return True
	else:
		return False
'''
#MAIN
str1 = "helleh"
str2 = "nurses run"
str3 = "what"

print(f"{str1} --> {palindrome(str1)}")
print(f"{str2} --> {palindrome(str2)}")
print(f"{str3} --> {palindrome(str3)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q7: PANGRAM: Write a function to check whether a string is a pangram or not.
#    Also assume string does not have punctuation 
#A7

import string

def ispangram(str1, alphabet=string.ascii_lowercase):

	#Create a set of the alphabet
	alphaset = set(alphabet)
	#Remove any spaces from the input
	str1 = str1.replace(' ','')
	#Convert into all lowercase
	str1 = str1.lower()
	#Grab all unique letters in lower case
	str1 = set(str1)
	#alphabet set == string set input
	return str1 == alphaset

str1 = "The quick brown fox jumps over the lazy dog"

print(f"{str1} --> {ispangram(str1)}")
