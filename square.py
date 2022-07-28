import math

class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
# Create method "is_valid" in the Square class
# This method checks if the square is valid
# True if the square is valid, False otherwise
    def is_valid(self,square_side):

        self.square_side=square_side
        if square_side==square_side:
            return True
        else:
            return False
        
# Create method "perimeter" in the Square class
# This method finds the perimeter of the square
# return perimeter of the square if the square is valid, 0 otherwise
    def perimetr(self,square_side):
        self.square_side=square_side
        if square_side==square_side:
            return 4*square_side
        else:
            return 0
# Create method "area" in the Square class
# This method finds the area of the square
# return area of the square if the square is valid, 0 otherwise
    def area(self,square_side):
        self.square_side=square_side
        if square_side==square_side:
            return square_side**2
        else:
            0
