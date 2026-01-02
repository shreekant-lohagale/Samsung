class Dog:
    def spark(self):
        return "Bark"

class Cat:
    def spark(self):
        return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.spark())

class Bike():
    def move(self):
        print("Bike is moving")

class Boat():
    def move(self):
        print("Boat is moving")

def trasportation(vehicle):
    vehicle.move()

trasportation(Bike())
trasportation(Boat())