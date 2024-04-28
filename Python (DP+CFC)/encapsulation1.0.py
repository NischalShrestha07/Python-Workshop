

# Encapsulation
# class name should always be named in PascalCase

class BankAccount:
    def __init__(self,accountNumber,_balance):
        self.__accountNumber=accountNumber
        self._balance=_balance
        # self.__accountNumber=accountNumber
    #  __accountNumber is the encapsulation which is done to not to let access the data outside the class
    # Encapsulation(__instance) kind of works like a private
     
    def deposit(self,amount):
         self._balance=self._balance+amount   
        #  self.balance+=amount  (ABOVE AND THIS BOTH ARE SAME) 
         print(f"Deposit Successful.New Balance: ${self._balance}")

        
    def checkBalance(self):
       print(f"Current Balance: ${self._balance}") 
   
   
    def withdraw(self,amount):
       self._balance= self._balance-amount
       print(f"Withdraw Successful. New Balance: $ {self._balance}")    


print("\n")
account=BankAccount('1254',10000)
account.checkBalance()
account.deposit(5000)
account.withdraw(5000)
# account.checkBalance()
# print(account.accountNumber)

