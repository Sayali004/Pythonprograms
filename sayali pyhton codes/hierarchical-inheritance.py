class language:
    def lang(self):
        print("I am a programming language")
class python(language):
    def py(self):
        print("I am python language")
class java(language):
    def jv(self):
        print("I am java language")
class c(language):
    def cplus(self):
        print("I am c++ language")

obj1 = python()
obj2 = java()
obj3 = c()

obj1.lang()
obj1.py()
obj2.lang()
obj2.jv()
obj3.lang()
obj3.cplus()
