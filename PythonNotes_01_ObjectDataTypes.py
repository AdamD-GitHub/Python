# Open Anaconda Prompt
# Run from D:\Program Files\SublimeText\PythonCode>
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# D:\Program Files\SublimeText\PythonCode>python PythonNotes.py 
# 
# Hot keys: cntl+s (save)

print("======================================")
print("- Print Format")
print("======================================")
#print lines
print("hello world")

#formatted print lines
name ="Sam"
age = 3
print("{n} is {a} years old.".format(n=name, a=age)) # old way
print(f"{name} is {age} years old.") #3.6+ way

print("")

print("======================================")
print("- Lists")
print("-    aka an Array")
print("-    --- USE BRACES [] ---")
print("-    Retrieved by INDEX")
print("-    Ordered sequence of objects (mutable)")
print("======================================")
#List in Python
mylist = [1,2,3] 
print(f"Position 0 value = {mylist[0]}")
print(f"Size of array: {len(mylist)}")

print("--- 1") #print list / reference list
mylist = ["one","two","three"]
print(f"Value at Position 0 = {mylist[0]}")
print(f"Value at Position 1,2 = {mylist[1:]}") #slicing 

print("--- 2") #concat two lists
another_list = ["four","five"]
print(f"Two lists concat = {mylist + another_list}")

print("--- 3") #concat and assign to new list variable
new_list = mylist + another_list
print(f"Two lists concat = {new_list}") 

print("--- 4") #Change list value
new_list[0] = "ONE ALL CAPS" 
print(f"Position 0 all CAPS = {new_list}") 

print("--- 5 (ADDING)") #Add element to list (.append)
new_list.append("six")
print(f"Add (.append) six = {new_list}") 

print("--- 6 (DELETING)") #Delete element to list (.pop)
new_list.pop #remove the last element
print(f"Delete (.pop) element = {new_list}")
pop_item = new_list.pop() #remove last element and store it in variable
print(f"Display deleted (.pop) element value = {pop_item}")
print(f"Delete (.pop) element = {new_list}")
new_list.pop(0) #removed from index
print(f"Delete (.pop) element = {new_list}")

print("--- 7 (SORTING)") #Sort elements in list 
new_list = ["a","e","x","b","c"]
num_list = [4,1,8,3]
print(f"Old List = {new_list}")
new_list.sort() #note this occurs in the list and does not return anything
print(f"Sorted List = {new_list}")
new_list.reverse()
print(f"Sorted List (reversed) = {new_list}")

#nested list example my_list[2][1]
print("")

print("======================================")
print("- Dictonaries")
print("-    aka an Array with key names")
print("-    --- USE BRACKETS {} ---")
print("-    Retrieved by KEY NAME")
print("-    Key value pairing that is unordered")
print("-    CANNOT sort a dictonaty because they are mappings")
print("======================================")
print("--- 1") #print value
prices_lookup = {"apple":2.99,"oranges":1.99,"milk":5.80}
print(f"Price of milk = {prices_lookup['milk']}")
print("--- 2") #multiple items within a dictonary
d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(f"index 2 of k2 = {d['k2'][2]}")
print("--- 3 (ADDING)") #adding values to a dictonary
d = {'k1':100,'k2':200}
print(f"d = {d}")
d['k3'] = 300
print(f"d = {d}")
print("--- 4 (OVERRIDING)") #overidding a value to a dictonary
d['k1'] = 'NEW VALUE'
print(f"d = {d}")
print("--- 5 (USEFUL METHODS)") 
d['k1'] = 100
print(f"d = {d}")
print(f"d.keys() = {d.keys()}") #return keys
print(f"d.values() = {d.values()}") #return values
print(f"d.items() aka Tuple= {d.items()}") #returns pairings (Tuple)
print("")

print("======================================")
print("- Tuples (contant list)")
print("-    aka a Static Array")
print("-    --- USE PARENTHESIS () ---")
print("-    Retrieved by INDEX")
print("-    Ordered sequence of objects (immutable)")
print("-    More advanced programming used to pass unchangeable objects")
print("======================================")
t = (1,2,'three',4,4)
mylist = [1,2,'three',4,4]
print("--- 1")
print(f"t = type {type(t)} {t}")
print(f"mylist = type {type(mylist)} {mylist}")
print("--- 2 (USEFUL METHODS)")
print(f"t.count(4) = {t.count(4)}") #how many times a value is in a Tuple
print(f"t.index(4) = {t.index(4)}") #first index location the value occurs
print("")

print("======================================")
print("- Sets")
print("-    aka an Array with NO duplicates")
print("-    --- USE BRACKETS {} ---")
print("-    Unordered collections of unique elements")
print("-    Notice no key value pairs")
print("======================================")
myset = set()
print("--- 1 (ADDING)") #adding values to a set
myset.add(1)
print(f"myset.add(1) = {myset}") 
myset.add(2)
myset.add(2) #notice trying to add a value which is already in there 
myset.add(3)
print(f"myset.add(1) = {myset}") 
print("")

print("======================================")
print("- Booleans")
print("-    Have cap T/F/N")
print("-    None is a boolean value for a placeholder")
print("======================================")
b = None
print(f"b = {b}") #adding values to a set
