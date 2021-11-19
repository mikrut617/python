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
        self.pet.play()
        return self

    def feed(self):
        
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
        else: 
            print("Oh no!!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.noise()


class Pet:

# implement __init__( name , type , tricks ):

    def __init__(self, name, cat_type, tricks, noise):
        self.name = name
        self.cat_type = cat_type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

# implement the following methods:
# sleep() - increases the pets energy by 25

    def sleep(self):
        self.energy += 25
        return self

# eat() - increases the pet's energy by 5 & health by 10

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

# play() - increases the pet's health by 5

    def play(self):
        self.health += 5
        return self

# noise() - prints out the pet's sound

    def noise(self):
        print(self.noise)


my_treats = ['Asparagus', 'Temptations', 'Blueberries']
my_pet_food = ['Kibbles', 'Yogurt']

marcus = Pet("Marky Mark", "Tuxedo Cat", ['bites ankles', 'chasing other cat', 'hiding'], "Meowwwwww!")

maciek = Ninja("Maciek", "Brzakala", my_treats, my_pet_food, marcus) 

maciek.feed();
maciek.feed();
maciek.feed();

