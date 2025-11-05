class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __repr__(self):
        return f"Num({self.value})"

a = MyNumber(10)
b = MyNumber(5)

c = a + b

print(c)