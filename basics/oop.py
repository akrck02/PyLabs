class Animal : 
    def __init__(self,name):
        self.name = name
        self.legs = 4

    def communicate(self): 
        print("Animal : GRRRRR")

    def eat(self):
        print("Animal: *eating grass*")

class Dog(Animal):

    def communicate(self):
        print("Dog " + self.name + ": wof!") 

    def eat(self):
        print("Dog " + self.name + ": *Eating steak*")

class Fish(Animal):

    def communicate(self): 
        print("Fish " + self.name + ": Blob!")

    def eat(self): 
        print("Fish " + self.name + ": Eating plakton!")

animals = [];

animals.append(Dog("Juan"));
animals.append(Fish("Nemo"));

for animal in animals: 
    animal.communicate();
    animal.eat();
    
