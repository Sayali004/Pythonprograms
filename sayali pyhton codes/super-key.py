
class Animal:
    def __init__(self):
        print("Animal is created")
    def category(self):
        print("I am an animal")
class WildAnimal(Animal):
    def __init__(self):
        super().__init__()
        print("Wild Animal is created")
    def wildInfo(self):
        print("I am a wild animal")
class Lion(WildAnimal):
    def __init__(self):
        super().__init__()
        print("Lion is created")
    def lionInfo(self):
        print("I am a lion")

obj = Lion()
obj.category()
obj.wildInfo()
obj.lionInfo()



    
    

