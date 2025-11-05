class Example:
    def say_hello(self, name=None):
        if name:
            print("Hello", name)
        else:
            print("Hello")

obj = Example()

obj.say_hello()       
#obj.say_hello("John")  
