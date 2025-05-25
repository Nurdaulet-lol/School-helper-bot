class Animal:
    def speak(self,speak):
         self.speak=speak

    def describe(self):
        print(f"This is a {self.__class__.__name__}.")

class Dog(Animal):
    def speak(self):
        print(" says: Woof!")

class Cat(Animal):
    def speak(self):
        print(" says: Meow!")

class Parrot(Animal):
    def speak(self):
        print(" says: I'm a pirate!")


animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    animal.speak()
    animal.describe()