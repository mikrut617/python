class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method  
    def walk(self):
        pass

    def feed(self):
        pass

    def bathe(self):
        pass

class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        pass

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        pass

    # play() - increases the pet's health by 5

    def play(self):
        pass

    # noise() - prints out the pet's sound
    def noise(self):
        print("Meow")



maciek = Ninja("Maciek") 
marcus = Pet("Marcus")