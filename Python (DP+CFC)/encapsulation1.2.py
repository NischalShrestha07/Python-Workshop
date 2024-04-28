

class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber=accountNumber
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposit SuccessFul.\nNew Balance: ${self.balance}")
    
    
    def checkBalance(self):
        print(f"Current Balance: {self.balance}")    
    def transferAmount(self,send):
        self.balance=self.balance-send
        print(f"Transfered Successful.\nNew balance:{self.balance}")
    
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print(f"Withdraw SuccessFul\nNew Balance: {self.balance}")


print("\n")        
account=BankAccount("12540",10000)
# account.checkBalance()
# account.withdraw(5000)
account.transferAmount(5000)
account.deposit(30000)
account.withdraw(50000)