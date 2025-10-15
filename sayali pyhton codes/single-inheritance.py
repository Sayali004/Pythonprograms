class Vehicle:
    def vehicleInfo(self):
        return "This is a vehicle"
    
class Car(Vehicle):
    def carInfo(self):
        return "This is a car"
    
obj1 = Car()
print(obj1.vehicleInfo())
print(obj1.carInfo())