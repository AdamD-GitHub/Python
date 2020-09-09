
#Q1: LESSER OF TWO EVENS: Write a function that returns the lesser of two given 
#    numbers if both numbers are even, but returns the greater if one or both 
#    numbers are odd
#A1

def lesser_of_two_evens(x1,x2):

    if x1%2 == 0 and x2%2 == 0:		#even number
   		return min(x1,x2)
    else:							#one or more odd number
    	return max(x1,x2)

#MAIN
num1 = 2
num2 = 4
num3 = 5

print(f"lesser of two evens({num1},{num2}) --> {lesser_of_two_evens(num1,num2)}")
print(f"lesser of two evens({num1},{num3}) --> {lesser_of_two_evens(num1,num3)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q2: ANIMAL CRACKERS: Write a function takes a two-word string and 
#    returns True if both words begin with same letter
#A2

def animal_crackers(text):
	animal_list = text.upper().split()

	return animal_list[0][0] == animal_list[1][0]

	#print (f"{animal_list[0][0]}")
	#print (f"{animal_list[1][0]}")

#	if (animal_list[0][0]).upper() == (animal_list[1][0]).upper():
#		return True
#	else:
#		return False




#MAIN
str1 = 'Levelheaded llama'
str2 = 'Crazy Kangaroo'

print(f"{str1} --> {animal_crackers(str1)}")
print(f"{str2} --> {animal_crackers(str2)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q3: MAKES TWENTY: Given two integers, return True if the sum of the 
#    integers is 20 or if one of the integers is 20. If not, return False
#A3

def makes_twenty(num_1,num_2):

	return (num_1 + num_2) == 20 or num_1 == 20 or num_2 == 20

#	if num_1 == 20 or num_2 == 20:
#		return True
#	elif (num_1 + num_2) == 20:
#		return True
#	else:
#		return False

#MAIN
num20 = 20
num10 = 10
num12 = 12
num8 = 8
num2 = 2
num3 = 3


print(f"{num20},{num10} --> {makes_twenty(num20,num10)}")
print(f"{num12},{num8} --> {makes_twenty(num12,num8)}")
print(f"{num2},{num3} --> {makes_twenty(num2,num3)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q4: OLD MACDONALD: Write a function that capitalizes the first and 
#    fourth letters of a name
#A4

def old_macdonald(str1):

	first_half = str1[:3]
	second_half = str1[3:]

	return first_half.capitalize() + second_half.capitalize()

#	first_letter = str1[0]
#	inbetween= str1[1:3]
#	fourth_letter = str1[3]
#	rest = str1[4:]
#
#	return first_letter.upper() + inbetween + fourth_letter.upper() + rest
#   ------------
#	index_ct = 0
#	mod_str = ""
#
#	for letter in str1:
#		index_ct += 1
#		if index_ct == 1 or index_ct == 4:
#			mod_str += letter.upper()
#		else:
#			mod_str += letter
#	
#	return mod_str

#MAIN
str1 = 'macdonald'

print(f"{str1} --> {old_macdonald(str1)}")


#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q5: MASTER YODA: Given a sentence, return a sentence with the words reversed
#A5

def master_yoda(str1):	
	yoda_list = str1.split()
	reverse_yoda_list = yoda_list[::-1]		#reverse a list
	return ' '.join(reverse_yoda_list)		#joins list elements together

#	mod_str = ""
#	yoda_list = str1.split()
#
#	for word in reversed(yoda_list):
#		mod_str += word
#		if yoda_list.index(word) == 0:		#check the index value in a list
#			pass
#		else:
#			mod_str += ' '
#	
#	return mod_str

#MAIN
yoda1 = 'home am I'
yoda2 = 'ready are we'

print(f"'{yoda1}' --> {master_yoda(yoda1)}")
print(f"'{yoda2}' --> {master_yoda(yoda2)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q6: ALMOST THERE: Given an integer n, return True if n is within 10 of either
#    100 or 200
#A6

def almost_there(num1):
	
	return 	((abs(num1 - 100) <= 10) or (abs(num1 - 200)) <= 10)


#	check_100 = abs(num1 - 100)
#	check_200 = abs(num1 - 200)
#	return check_100 <= 10 or check_200 <= 10

#	if check_100 <= 10 or check_200 <= 10:
#		return True
#	else:
#		return False


#MAIN
num1 = 90
num2 = 104
num3 = 150
num4 = 209

print(f"'{num1}' --> {almost_there(num1)}")
print(f"'{num2}' --> {almost_there(num2)}")
print(f"'{num3}' --> {almost_there(num3)}")
print(f"'{num4}' --> {almost_there(num4)}")


#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q7: Given a list of ints, return True if the array contains a 3 next to a
#    3 somewhere
#A7

def has_33(nums):
	for i in range(0,len(nums)-1):
		if nums[i] == 3 and nums [i+1] == 3:  #also used if nums[i:i+2]==[3,3]
			return True

	return False

#MAIN
list1 = ([1,3,3])
list2 = ([1,3,1,3])
list3 = ([3,1,3])

print(f"'{list1}' --> {has_33(list1)}")
print(f"'{list2}' --> {has_33(list2)}")
print(f"'{list3}' --> {has_33(list3)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q8: PAPER DOLL: Given a string, return a string where for every character
#    there are three characters
#A8

def paper_doll(text):
	result = ''

	for char in text:
		result += char*3
	return result

#MAIN
str1 = "hello"
str2 = "Mississippi"

print(f"'{str1}' --> {paper_doll(str1)}")
print(f"'{str2}' --> {paper_doll(str2)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q9: BLACKJACK: Given three integers between 1 and 11, if their sum is less 
#    than or equal to 21, return their sum.  If it exceeds 21 and there's an 11
#    reduce the total sum by 10.  Finally, if the sum exceeds 21, return BUST
#A9

def black_jack(a,b,c):
	
	if sum([a,b,c]) <= 21:
		return sum([a,b,c])
	elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:
		return sum([a,b,c])-10
	else:
		return 'BUST'

#MAIN
print(f"'{list1}' --> {black_jack(5,6,7)}")
print(f"'{list2}' --> {black_jack(9,9,9)}")
print(f"'{list3}' --> {black_jack(9,9,11)}")

#-----------------------------------------------------------------
print(f'-----------')
#-----------------------------------------------------------------
#Q10: SUMMER OF 69: Return the sum of the numbers in the array, ecept ignore 
#     sections of numbers starting with a 6 and extending to the next 9 (every
#     6 will be followed by at least on 9).  Return 0 for no numbers.
#A10

def summer_69(arr):
	
	total = 0
	add = True

	for num in arr:
		while add:
			if num != 6:
				total += num
				break
			else:
				add = False
		while not add:
			if num != 9:
				break
			else:
				add = True
				break
	return total


#MAIN
list1 = (1,3,5)
list2 = (4,5,6,7,8,9)
list3 = (2,1,6,9,11)

print(f"'{list1}' --> {summer_69(list1)}")
print(f"'{list2}' --> {summer_69(list2)}")
print(f"'{list3}' --> {summer_69(list3)}")