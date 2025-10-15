class Student:
    def __init__(self, name=None, age=None):
        if name and age:
            print("Name:", name, "Age:", age)
        elif name:
            print("Name:", name)
        else:
            print("No information given")

s1 = Student()
s2 = Student("Shravani")
s3 = Student("Shravani", 21)
