#To creat the BankAccount class
class bank:
   def __init__(self):
       self.balance=0
       print("Welcome to the SBI")
       
   def deposite(self):
       amount=float(input("Enter the amount to be Deposited:"))
       self.balance +=amount
   def withdraw(self):
     amount = float(input("Enter amount to be withdraw:"))
     if self.balance>=amount:
         self.balance-=amount
         print("\nYou Withdraw:",amount)
     else:
         print("\nInsufficient balance")
   def display(self):
         print("\nNet Available Balance =",self.balance)
#drive code
s=bank()
s.deposite()
s.withdraw()
s.display()

         
