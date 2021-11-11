class User: #Syntax for creating a class we want to call User
    pass 

# declare a class and give it name User
class User:		
    # Instance attributes are defined in a "magic method" called __init__, which is called when a new object is instantiated.
    def __init__(self, name, email, account_balance, make_withdrawl, _display_user_balance):
        # The first parameter of an instance method within a class will be self, and the instance attributes are also indicated by self..
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0
        self.make_wtihdrawl = 0
        self.display_user_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount

michael = User("Michael Jordan", "mj@bulls.com")
kobe = User("Kobe Bryant", "kb@lakers.com")
shaq = User("Shaq", "shaq@tnt.com")
print(michael.name)
print(shaq.name)	    