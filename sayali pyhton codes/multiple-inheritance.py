class Parent1:
    def func1(self):
        print("This is function 1 from Parent1")

class Parent2:
    def func2(self):
        print("This is function 2 from Parent2")

class Child(Parent1, Parent2):
    def func3(self):
        print("This is function 3 from Child")

obj = Child()
obj.func1()
obj.func2()
obj.func3()

