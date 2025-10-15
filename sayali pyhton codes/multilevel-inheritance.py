class car:
    def carInfo(self):
        return "This is a car"
class SUV(car):
    def fortunerInfo(self):
        return "This is a SUV"
class Ford(SUV):
    def fordInfo(self):
        return "This is a Ford"

object1 = Ford()
print(object1.carInfo())
print(object1.fortunerInfo())
print(object1.fordInfo())
