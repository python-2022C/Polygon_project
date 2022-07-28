import math

class Circle:
    def __init__(self, radius:float):
        self.r = radius
    # Create method "is_valid" in the Circle class
    # This method checks if the circle is valid
    # True if the circle is valid, False otherwise

    # Create method "diameter" in the Circle class
    # This method finds the diameter of the circle
    # return diameter of the circle if the circle is valid, 0 otherwise

    # Create method "circumference" in the Circle class
    # This method finds the circumference of the circle
    # return circumference of the circle if the circle is valid, 0 otherwise

    # Create method "area" in the Circle class
    # This method finds the area of the circle
    def area(self,radius):
    self.radius = radius
    return self.radius**2*math.pi
    # return area of the circle if the circle is valid, 0 otherwise
    def is_valid(self):
        return self.r > 0


