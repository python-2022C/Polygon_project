import math

class Circle:
    def __init__(self, radius:float):
        self.radius = radius
    
    def is_valid(self) -> str:
        return bool(self.radius)

circle = Circle(4)
is_valid_circle = circle.is_valid()
print("Can it be a circle?", is_valid_circle)

# Create method "diameter" in the Circle class
# This method finds the diameter of the circle
# return diameter of the circle if the circle is valid, 0 otherwise

# Create method "circumference" in the Circle class
# This method finds the circumference of the circle
# return circumference of the circle if the circle is valid, 0 otherwise

# Create method "area" in the Circle class
# This method finds the area of the circle
# return area of the circle if the circle is valid, 0 otherwise
