import math
from typing_extensions import Self

class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
        

    # Create method "is_valid" in the Rectangle class
    # This method checks if the rectangle is valid
    # True if the rectangle is valid, False otherwise
    def is_valid(self, a, b):
        if self.a >0 and self.b >0:
            return True
        else:
            return False
        

    # Create method "perimeter" in the Rectangle class
    # This method finds the perimeter of the rectangle
    # return perimeter of the rectangle if the rectangle is valid, 0 otherwise
    def perimeter(self, a,b):
        if self.a >0 and self.b>0:
            return 2*a+2*b
        else:
            return 0

    # Create method "area" in the Rectangle class
    # This method finds the area of the rectangle
    # return area of the rectangle if the rectangle is valid, 0 otherwise
    def area(self, a, b):
        if self.a >0 and self.b>0:
            return a*b
        else:
            return 0