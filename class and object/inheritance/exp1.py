class Dog:
    def spark(self):
        return "Bark"

class Cat:
    def spark(self):
        return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.spark())