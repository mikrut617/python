## ENCAPSULATION ##

# Encapsulation is the idea that we can group code together into objects; hence Object Oriented Programming. We use classes or "coding blue prints" to define what our objects are and how they behave. We encapsulate attributes and methods in our class.

## Example:

# class CoffeeM:
#     def __init__(self,name):
#         self.name = name
#         self.water_temp = 200
#     def brew_now(self,beans):
#         print(f"Using {beans}!")
#         print("Brew now brown cow!")
#     def clean(self):
#         print("Cleaning!")


## INHERITANCE ##

# Inheritance is the idea that we pass along attributes and methods from one class into a "sub-class" or child class, and not have to re-write the code to make it work.  Child classes can be more specific versions of their Parent class.  Using the key word "super" will call methods

# class CappuccinoM( CoffeeM ):
#     def __init__(self,name):
#         super().__init__(name)
#         self.milk = "whole"
#     def make_cappuccino(self,beans):
#         super.brew_now(beans)
#         print("Frothy!!!")


## POLYMORPHISM ##

# Polymorphism means "many forms", and the idea in OOP is that a Child class can have a different version of a method than the Parent class. In this example the child class of CappuccinoM has a clean method, and so does CoffeeM. Depending on the class, the clean method will do different things.

# class CappuccinoM( CoffeeM ):
#     def __init__(self,name):
#         super().__init__(name)
#         self.milk = "whole"
#     def make_cappuccino(self,beans):
#         super.brew_now(beans)
#         print("Frothy!!!")
#     def clean(self):
#         print("Cleaning the froth!")


## ABSTRACTION ##

# class Barista:
#     def __init__(self,name):
#         self.name = name
#         self.cafe = CoffeeM("Cafe")
#     def make_coffee(self):
#         self.cafe.brew_now()


### If you want to write it manually, this is cumbersom and not best practice

# pie_one = {'name' : 'Apple Pie', 'topping' : 'Ice Cream', 'season_avail' : 'fall'}
# pie_two = {'name' : 'Cherry Pie', 'topping' : 'Whipped Cream', 'season_avail' : 'spring'}
# pie_three = {'name' : 'Pumpkin Pie', 'topping' : 'Ready Whip', 'season_avail' : 'fall'}

# pie_four = {'name' : 'Pumpkin Pie', 'topping' : 'Ready Whip', 'season_avail' : 'fall'}



# Example of Four Pillars

class Dessert:
    store_name = "Maciek's Pastries"
    def __init__(self, name, ingredients, season, qty):
        self.name = name
        self.ingredients = ingredients
        self.season = season
        self.qty = qty

    def topping(self):
        return "None"

    def addSide(self, side):
        self.side = side
        return self

class Pie(Dessert): 
    def __init__(self, name, ingredients, season, qty):
        super().__init__(name, ingredients, season, qty)

    def topping(self):
        self.topping = "None"
        return "Ice Cream" ## add this so not every pie we offer comes with ice cream

class Pastry(Dessert):
    def __init__(self, name, ingredients, season, qty):
        super().__init__(name, ingredients, season, qty)

    def topping(self):
        return "Whipped Cream"

class Cake(Dessert):
    def __init__(self, name, ingredients, season, qty):
        super().__init__(name, ingredients, season, qty)

    def topping(self):
        return "Butter Cream"

    def amount(self):
        if self.qty < 6:
            return "No Box"
        elif self.qty < 36:
            return "Needs Box"
        else:
            return "Needs Carton"

apple_pie = Pie("Apple Pie", "Apples", "Fall", 1)
print(apple_pie.name)
print(apple_pie.topping())

canoli = Pastry("Canoli", "Canoli", "4 Season", 12)
print(canoli.name)

carrot_cake = Cake("Carrot Cake", "Carrot", "All year", 5)
print(carrot_cake.amount())

# pie_one = Pie("Pizza Pie", "Thin", "10", "Cheese",  "Personal")
# print(pie_one.topping)

# pie_one.addTopping("Sausage")
# print(pie_one.topping)

# pie_two = Pie("Sheppards Pie", "Thick", 10, "Potatoes", "Large")
# pie_two.addSide("Buffalo Wings")
# print(pie_two.side)


# pie_three = Pie("Sweet Potato Pie", "Marshmallows", "Thick", 15)
# print(pie_three.name)

# pie_three.addTopping("Marshmallows").addTopping("Brown Sugar").addSide("Bacon")
# print(pie_three.topping)

# print(pie_two.size)
# print(pie_two.topping)


