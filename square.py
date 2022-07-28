import math

class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    def is_valid(self):
        if self.square_side > 0:
            return True
        return False
    def perimeter(self):
        if self.is_valid():
            return self.square_side * 4
        return 0
    def area(self):
        if self.is_valid():
            return pow(self.square_side,2)
        return 0
    
# Create method "is_valid" in the Square class
# This method checks if the square is valid
# True if the square is valid, False otherwise

# Create method "perimeter" in the Square class
# This method finds the perimeter of the square
# return perimeter of the square if the square is valid, 0 otherwise

# Create method "area" in the Square class
# This method finds the area of the square
# return area of the square if the square is valid, 0 otherwise
