class BankAccount:
    accounts = [] # BONUS question

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.accounts.append(self) #BONUS questions

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self

    @classmethod  ## BONUS question ##
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = BankAccount(.05, 2000)
savings = BankAccount(.0124, 10000)

checking.deposit(50).deposit(10).deposit(10).withdraw(500).yield_interest().display_account_info()
savings.deposit(200).deposit(1050).deposit(135).withdraw(90).yield_interest().display_account_info()

## BONUS question
BankAccount.print_all_accounts()