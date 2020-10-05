# Open Anaconda Prompt
# Navigate to code directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart


#NOTE: You MUST create a folder in each package called __init__.py so Python knows it is a package

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#IMPORT FROM A MODULE

from PythonNotes_09_MyModule import my_func

my_func()

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#IMPORT FROM A PACKAGE AND SUBPACKAGE

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.report_sub()

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------

if __name__ == '__main__':
	print("PythonNotes_09_MyProgram.py is being run directly")
else:
	print("PythonNotes_09_MyProgram.py is NOT being run directly")