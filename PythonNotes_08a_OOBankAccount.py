# Open Anaconda Prompt
# Navigate to code directory
# Once in the directory, type - python ****.py (You can use [tab] to fill it in)
# C:\PythonCode>python PythonNotes.py
# 
# Hot keys: cntl+s (save)
# If testing with Junyper and need to restart: Kernel - Restart - Restart

#---------------------------------------------
print("\n-------\n")
#---------------------------------------------
'''
Creata a bank account class that has two attributes:
- Owner
- Balance
and two methods
- Deposit
- Withdraw
As an added requirement, withdrawals may not exceed the available balance.
'''


class Account:

	def __init__(self,owner,balance=0):
		
		self.owner = owner			
		self.balance = balance

	def __str__(self):			
		
		return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"

	def deposit(self,dep):

		self.balance += dep
		print(f"${dep} - Deposit Accepted")

	def withdraw(self,wthdl):
		
		self.balance_check = self.balance - wthdl

		if self.balance >= wthdl:
			self.balance -= wthdl
			print(f"${wthdl} - Withdrawal Accepted")
		else:
			print(f"${wthdl} -Funds Unavailable")

#main
acct1 = Account('Jose',100)

print(acct1.owner)
print(acct1.balance)
print(acct1)

acct1.deposit(50)
print(acct1)

acct1.withdraw(75)
print(acct1)

acct1.withdraw(500)
print(acct1)
