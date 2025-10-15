#default constructor
class Person:
  def __init__(self):
    self.name = "Shravani"
    self.age = 21

p1 = Person()
print(p1.name)
print(p1.age)

#parameterized constructor
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Kiran", 25)
print(p1.name)
print(p1.age)

#destructor
class Sample:
    def __init__(self):
        print("Constructor is called")
        
    def __del__(self):
        print("Destructor is called")
obj = Sample()
del obj
