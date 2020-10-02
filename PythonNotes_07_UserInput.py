# Open Anaconda Prompt
# Run from D:\Program Files\SublimeText\PythonCode>
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# D:\Program Files\SublimeText\PythonCode>python PythonNotes.py 
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart


#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
#Local - scope is inside lambda statements

def user_choice():
	choice = 'WRONG'			#Use this to force a digit until true
	acceptable_range = range(0,10)
	within_range = False

	while choice.isdigit() == False or within_range == False:
		choice = input("Please enter a number (0-9): ")

		#DIGIT CHECK
		if choice.isdigit() == False:
			print("Sorry that is not a digit!")

		#RANGE CHECK
		if choice.isdigit() == True:
			if int(choice) in acceptable_range:
				within_range = True
			else:
				print("Sorry you are out of acceptable range (0-9)")
				within_range = False
		
	return int(choice)

#MAIN
print (f"You entered {user_choice()}")

