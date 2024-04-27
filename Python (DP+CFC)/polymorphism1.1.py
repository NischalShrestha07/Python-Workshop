class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woooof Wooou"
class Cat(Animal):
    def speak(self):
        return "Meowww Meow"


def makeSound(animal):
    print(animal.speak())

animals=[Dog(),Cat()]
for animal in animals:
    makeSound(animal)