class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):  
        print("Woof!")

class Cat(Animal):
    def speak(self):  
        print("Meow!")

my_dog = Dog()
my_cat = Cat()

my_dog.speak()
my_cat.speak()