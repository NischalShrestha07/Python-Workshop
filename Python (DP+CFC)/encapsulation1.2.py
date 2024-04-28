

class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber=accountNumber
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposit SuccessFul. New Balance: ${self.balance}")
    
    
    def checkBalance(self):
        print(f"Current Balance: {self.balance}")    
    
    
    def withdraw(self,amount):
        self.balance=self.balance-amount


print("\n")        
account=BankAccount("12540",100000)
account.checkBalance()
