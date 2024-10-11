def area(self):
      import math
      return math.pi * self.radius ** 2

def perimeter(self):
      import math
      return 2 * math.pi * self.radius

def print_shape_info(shape):
   print(shape.description())
   print(f"Area: {shape.area()}")
   print(f"Perimeter: {shape.perimeter()}")

shapes = [Rectangle(5, 10), Circle(7)]

for shape in shapes:
   print_shape_info(shape)
   print("-" * 20)

class IncompleteShape(Shape):
   pass

try:
   incomplete_shape = IncompleteShape()
except TypeError as e:
   print(e)  