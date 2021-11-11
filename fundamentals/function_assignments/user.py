class User:		

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


michael = User("Michael Jordan")
kobe = User("Kobe Bryant")
shaq = User("Shaq")


michael.make_deposit(1000000)
michael.make_deposit(4534534)
michael.make_deposit(98745873)
michael.make_withdrawl(124234)
michael.display_user_balance()

kobe.make_deposit(56756)
kobe.make_deposit(12343646776976)
kobe.make_withdrawl(64756)
kobe.make_withdrawl(6585345236563)
kobe.display_user_balance()

shaq.make_deposit(123456789)
shaq.make_withdrawl(123)
shaq.make_withdrawl(456)
shaq.make_withdrawl(789)
shaq.display_user_balance()

michael.transfer_money(100, shaq)