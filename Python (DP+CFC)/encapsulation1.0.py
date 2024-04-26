

# Encapsulation
# class name should always be named in PascalCase

class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber=accountNumber
        self.balance=balance
     
     
     
    def deposit(self,amount):
         self.balance=self.balance+amount   
        #  self.balance+=amount  (ABOVE AND THIS BOTH ARE SAME) 
         print(f"Deposit Successful.New Balance: ${self.balance}")

        
    def checkBalance(self):
       print(f"Current Balance: ${self.balance}") 
   
   
    def withdraw(self,amount):
       self.balance= self.balance-amount
       print(f"Withdraw Successful. New Balance: $ {self.balance}")    


print("\n")
account=BankAccount('1254',10000)
account.checkBalance()
account.deposit(5000)
account.withdraw(5000)
# account.checkBalance()