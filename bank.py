class Bank:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. New balance:", self.balance)
        else:
            print("Invalid deposit amount.")

    def show_balance(self):
        print("Current balance:", self.balance)


my_bank = Bank(1000)  


my_bank.show_balance()  
my_bank.deposit(500)    
my_bank.withdraw(200)   
my_bank.show_balance()  
