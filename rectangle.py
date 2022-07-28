import math

class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    # Create method "is_valid" in the Rectangle class
    # This method checks if the rectangle is valid
    # True if the rectangle is valid, False otherwise
    def is_valid(self):
        """
        returns area of rectangle -> (bool)
        """ 
        a = self.a
        b = self.b
        return a > 0 and b > 0

    # Create method "perimeter" in the Rectangle class
    # This method finds the perimeter of the rectangle
    # return perimeter of the rectangle if the rectangle is valid, 0 otherwise
    def perimeter(self):
        """
        returns area of rectangle -> (float)
        """
        a = self.a
        b = self.b
        if self.is_valid():
            return float(a*2 + b*2)
        else:
            return 0

    # Create method "area" in the Rectangle class
    # This method finds the area of the rectangle
    # return area of the rectangle if the rectangle is valid, 0 otherwise
    def area(self):
        """
        returns peremets of rectangle -> (float)
        """
        a = self.a
        b = self.b
        if self.is_valid():
            return float(a * b)
        else:
            return 0