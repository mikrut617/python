class User: #Syntax for creating a class we want to call User
    pass 

# declare a class and give it name User
class User:		
    # Instance attributes are defined in a "magic method" called __init__, which is called when a new object is instantiated.
    def __init__(self):
        # The first parameter of an instance method within a class will be self, and the instance attributes are also indicated by self..
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# Now we can create instances of the User:
User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

# We can also set the values for our instance's attributes:
guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty

# Class attributes are defined outside of any instance methods, and is shared among all instances of the class.  
# Class attributes are more flexible because we can change them on an instance or the entire class.

class User:
# declaring a class attribute
    bank_name = "First National Dojo"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# Changing them on an instance:  
guido = User()
monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union 
print(monty.bank_name) # output: First National Dojo

# Changing them on the entire class:
User.bank_name = "Bank of Dojo"
print(guido.bank_name) # output: Bank of Dojo 
print(monty.bank_name) # output: Bank of Dojo


# While we definitely want every user to have a name, email, and account balance, we don't want all of our users to have the same name and email address upon creation. How will we know what the name should be?
# We can pass in arguments into the __init__ method to specify a user's instance attributes.


class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
# now our method has 2 parameters!
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python


# Now it's time to add some functionality to our class. Methods are just functions that belong to a class.
# For example, if a user wanted to make a deposit, we'd want to be able to call the method from the user instance; because a specific user is making a deposit, it should only affect that user's balance.
# The call would look like this --> guido.make_deposit(100)

# To be able to call on this method, it needs to exist.

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

# Now that our method is written, we can call it:

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50




