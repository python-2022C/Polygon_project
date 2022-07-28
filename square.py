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
