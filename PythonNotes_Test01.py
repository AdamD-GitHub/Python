import math

#Q1-3: Answer these 3 questions without typing code. 
#    Then type code to check your answer.

answer01 = 4*(6+5)
answer02 = 4*6+5
answer03 = 4+6*5
print(f"answer01 = {answer01}\nanswer02 = {answer02}\nanswer03 = {answer03}")

print(f'-----------')
#-----------------------------------------------------------------
#Q4: What is the type of the result of the expression 3 + 1.5 + 4?

answer04 = 3+1.5+4
print(f"answer04 = {type(answer04)}")

print(f'-----------')
#-----------------------------------------------------------------
#Q5-6: What would you use to find a number’s square root, as well as its square?

answer05 = math.sqrt(9)
answer06 = 9**2
print(f"answer05 = {answer05}")
print(f"answer06 = {answer06}")

print(f'-----------')
#-----------------------------------------------------------------
#Q7-10: Given the string 'hello' give an index command that returns 'e'. 
#       Reverse the string 'hello' using slicing
#       Given the string hello, give two methods of producing the 
#          letter 'o' using indexing

s = 'hello'
print(f"s = {s[1]}")
print(f"s = {s[::-1]}") #reverse the order - uses step size -1
print(f"s = {s[-1]}")
print(f"s = {s[4]}")

print(f'-----------')
#-----------------------------------------------------------------
#Q11-14: Build this list [0,0,0] two separate ways
#        Reassign 'hello' in this nested list to say 'goodbye' instead
#        Sort the list below (list4)

print(f"---- List ---")
list1 = [0,0,0]
list2 = [0]
list3 = [1,2,[3,4,'hello']]  
list4 = [5,3,4,6,1]
list2.append(0)
list2.append(0)
list3[2][2] = 'goodbye'  #change hello to goodbye
list4.sort()
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")
print(f"list4 = {list4}")

print(f'-----------')
#-----------------------------------------------------------------
#Q15-18: Using keys and indexing, grab the 'hello' from the following dictionaries

print(f"---- Dictonary ---")
d = {'k1':{'k2':'hello'}}
#---
d1 = d['k1']
print(f"d = {d1['k2']}") #retrieve hello 
#---
print(f"d = {d['k1']['k2']}") #retrieve hello 


d = {'k1':[{'nest_key':['this is deep',['hello']]}]} #--> dictonary
#---
d1 = d['k1']
print(f"d = {d1}") #[{'nest_key':['this is deep',['hello']]}] --> list
d2 = d1[0]
print(f"d = {d2}") #{'nest_key':['this is deep',['hello']]} --> dictonary
d3 = d2['nest_key']
print(f"d = {d3}") #['this is deep',['hello']] --> list
d4 = d3[1]
print(f"d = {d4[0][0:]}") #retrieve hello 
#---
print(f"d = {d['k1'][0]['nest_key'][1][0]}") #retrieve hello 

print(f'-----------')
#-----------------------------------------------------------------
#Q19: Use a set to find the unique values of the list below

print(f"---- Set ---")
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(f"list5 = {set(list5)}") #cast a list into a set
