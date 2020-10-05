# Open Anaconda Prompt
# Navigate to doce directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)

print("======================================")
print("- Input/Output")
print("======================================")
print("")

print("======================================")
print("- Open File")
print("-    Need to make sure file is in same location")
print("======================================")
myfile = open('myfile.txt') #must be in ticks
print("--- 1 (FILEPATHS)")
#\\ so Python doesn't confuse escape characters
myfile2 = open("D:\\Program Files\\SublimeText\\PythonCode\\myfile.txt") 
print("")

print("======================================")
print("- Read")
print("-    Need to re-read, must reset index back to beginning")
print("======================================")
print("--- 1")
print(f"{myfile.read()}")
print("")
print(f"{myfile2.read()}")
print("")
print(f"{myfile.read()}") #file has already been read, must reset
myfile.seek(0)
print("")
print(f"{myfile.read()}")
myfile.seek(0)
print(f"{myfile.readlines()}")
myfile.seek(0)
print("")

print("======================================")
print("- Close File")
print("======================================")
myfile.close()
myfile2.close()
print("")

print("======================================")
print("- Open File -- BEST PRACTICES")
print("-    Also .read, .write")
print("======================================")
#using with open(), the file will automatically close
#in Jupyter Notebook, shift tab will give you more informaiton
#'mode=' is the permission which only allow you to:
#    read 'r', write 'w', append 'a', read/write 'r+', or write/read 'w+'
#    note 'w'/'w+' will overwrite or creaete new
with open('myfile.txt', mode='r') as myfile:
	contents = myfile.read()
print(f"{contents}")
print("")
with open('my_file.txt', mode='w') as f: 
	f.write('ONE ON FIRST\nTWO ON SECOND\nTHREE ON THRID')
with open('my_file.txt', mode='r') as f: #since file closes, no need for seek
	print(f.read())
print("")
with open('my_file.txt', mode='a') as f: 
	f.write('\nFOUR ON FORTH')
with open('my_file.txt', mode='r') as f: 
	print(f.read())
