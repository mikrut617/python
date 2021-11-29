## Polymorphic behavior allows us to specify common methods in an "abstract" level and implement them in particular instances. It is the process of using an operator or function in different ways for different data input.

# Use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways

class Person:
  def pay_bill(self):
      raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
  def pay_bill(self):
      print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
  def pay_bill(self):
      print("Can I owe you ten bucks or do the dishes?")


