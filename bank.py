class Account:
    school="AkiraChix"
    def __init__(self,account_name,account_number,password,balance) :
        self.account_name=account_name
        self.account_number=account_number
        self.password=password
        self.balance=balance
        self.deposits=[]
        self.withdrawals=[]


    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount must be greater than zero"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f" you have deposited {amount}. your new balance is {self.balance}"


    def withdraw(self,amount):
        if amount > self.balance:
            return f"your balance is {self.balance}, you cannot withdraw your balance is insuficient {amount}"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            self.withdrawals.append(amount)
            self.transaction_cost=100
            self.balance-=amount+ self.transaction_cost

            return f"Hello {self.account_name} you have withdrawn{amount} your new balance is {self.balance}",self.withdraw
    

    def deposit_statement(self):
        for depos in self.deposits:
            print(f"you have deposited{depos}")

    def withdrawals_statement(self):
        for withdraw in self.withdrawals:
            print (f"You have withrdrawn KES{withdraw}")


    def withdrawals(self, amount):
        if amount >0:
            self.balance-=amount+100
            return f"Hello {self.account_name}, you have withdraw{amount} and your new balance is {self.balance}"
        elif amount <0:
            return f"Withdraw amount must be greater than zero"
        elif amount == self.balance:
            return f"Insufficient"
        else:
            return f"Insufficient funds"            
    def current_balnce(self):
        return f"The current balance is KSH {self.balance}"

