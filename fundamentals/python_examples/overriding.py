# Sometimes the problem with implicit inheritance is that you want the child to behave completely differently than the parent. In these cases you want to override the function, effectively replacing the functionality. To do this, just define a function with the same name in the child class. Here's an example:

class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!

