
class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance 
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        self.balance -= amount 
        
        if amount > self.balance:
            self.balance -=5
            print("Insufficent Funds Charging a $5 fee")
        return self
    
    def display_account_info(self):
        self.balance
        print(f"Account: ${self.display_account_info()}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

Account1=BankAccount(.01, balance=0)
Account2=BankAccount(.01 , 0)

Account1.deposit(500).deposit(50).deposit(50).withdraw(100).yield_interest().display_user_balance()
Account2.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_user_balance()
print(Account1, Account2)