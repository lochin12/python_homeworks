class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        return f"{self.name} is being milked."  

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Klak")
    
    def lay_egg(self):
        return f"{self.name} laid an egg!"

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep", "Bee")
    
    def shear(self):
        return f"{self.name} is getting sheared for wool."

cow = Cow("Masha")
chicken = Chicken("Marusya")
sheep = Sheep("Baran")

animals = [cow, chicken, sheep]
for animal in animals:
    print(animal.make_sound())
    print(animal.eat("grass"))
    print(animal.sleep())
    
print(cow.produce_milk())
print(chicken.lay_egg())
print(sheep.shear())

