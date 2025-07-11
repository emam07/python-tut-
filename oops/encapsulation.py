
Account_no=int(input("Enter the bank account no "))
Deposit_money=int(input("Enter the amount to deposit"))
class BankAccount():
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
        print(f'{amount} Deposited successfully. \nnew balance {self.__balance}')
    
    def getbalance(self):
        return self.__balance
    

account=BankAccount(Account_no,10000)

account.deposit(Deposit_money)
print(account.getbalance())

