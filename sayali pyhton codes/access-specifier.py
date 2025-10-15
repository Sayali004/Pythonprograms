class Sample:
    publicVar = "I am Public"
    _protectedVar = "I am Protected"
    __privateVar = "I am Private"

obj = Sample()
print(obj.publicVar)
print(obj._protectedVar)
#print(obj.__privateVar)    #raise AttributeError

class Sample:
    def publicMethod(self):
        print("I am Public Method")
        
    def _protectedMethod(self):
        print("I am Protected Method")
        
    def __privateMethod(self):
        print("I am Private Method")
obj = Sample()
obj.publicMethod()
obj._protectedMethod()
#obj.__privateMethod()   #raise AttributeError