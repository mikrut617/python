from four_pillars import Dessert

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
