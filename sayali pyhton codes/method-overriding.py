class Shape:
    def no_of_sides(self):
        print("This shape has many sides")

class Square(Shape):
    def no_of_sides(self):
        print("A square has 4 sides")
    def area(self, side):
        return side * side
class Triangle(Shape):
    def no_of_sides(self):
        print("A triangle has 3 sides")
    def area(self, base, height):
        return 0.5 * base * height
    
sq = Square()
sq.no_of_sides()
print("Area of square:", sq.area(4))
tr = Triangle()
tr.no_of_sides()
print("Area of triangle:", tr.area(3, 6))
