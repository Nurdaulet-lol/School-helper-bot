class Animal:
    def speak(self,speak):
         self.speak=speak

    def describe(self):
        print(f"This is a {self.__class__.__name__}.")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

class Parrot(Animal):
    def speak(self):
        print("Parrot says: I'm a pirate!")


animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    animal.speak()
