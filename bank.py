class Account:
    school="AkiraChix"
    def __init__(self,account_name,account_number,password,balance) :
        self.account_name=account_name
        self.account_number=account_number
        self.password=password
        self.balance=balance


    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return self.balance

    def withdraw(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return f"Hello you've withrawn {amount}  from the account name {self.account_name} and the account number is {self.account_number} and your currebtbalance is {self.balance}"