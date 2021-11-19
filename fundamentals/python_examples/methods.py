class Pie: 
    store_name = "Maciek's Pies"
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

    @classmethod
    def name_change(cls, name):
        cls.store_name = name

Pie.name_change("Matt's Pie")

pie_one = Pie("Pizza Pie", "Thin", "10", "Cheese",  "Personal")
print(pie_one.store_name)
# print(pie_one.topping)


# pie_one.addTopping("Sausage")
# print(pie_one.topping)