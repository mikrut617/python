### If you want to write it manually, this is cumbersom and not best practice

# pie_one = {'name' : 'Apple Pie', 'topping' : 'Ice Cream', 'season_avail' : 'fall'}
# pie_two = {'name' : 'Cherry Pie', 'topping' : 'Whipped Cream', 'season_avail' : 'spring'}
# pie_three = {'name' : 'Pumpkin Pie', 'topping' : 'Ready Whip', 'season_avail' : 'fall'}

# pie_four = {'name' : 'Pumpkin Pie', 'topping' : 'Ready Whip', 'season_avail' : 'fall'}



# Blueprint for OOP # Use this instead of above

class Pie: 

    def __init__(self, name, topping, crust, price, size = 'personal'):
        self.name = name
        self.topping = topping
        self.crust = crust
        self.price = price
        self.size = size

    def addTopping(self, topping):
        self.topping = topping
        return self # When chaining below, you need to come back here and add return self

    def addSide(self, side):
        self.side = side
        return self


# pie_one = Pie("Pizza Pie", "Thin", "10", "Cheese",  "Personal")
# print(pie_one.topping)

# pie_one.addTopping("Sausage")
# print(pie_one.topping)

pie_two = Pie("Sheppards Pie", "Thick", 10, "Potatoes", "Large")
pie_two.addSide("Buffalo Wings")
print(pie_two.side)


pie_three = Pie("Sweet Potato Pie", "Marshmallows", "Thick", 15)
print(pie_three.name)

pie_three.addTopping("Marshmallows").addTopping("Brown Sugar").addSide("Bacon")
print(pie_three.topping)

# print(pie_two.size)
# print(pie_two.topping)