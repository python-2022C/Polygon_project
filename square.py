import math

class Square:
    def __init__(self, square_side:float):
        """
        is_valid() -> bool
        area() -> float
        perimeter() -> float
        """
        self.square_side = square_side

    def is_valid(self):
        """
        returns area of square -> (bool)
        """
        a = self.square_side 
        return a > 0

    def area(self)-> bool:
        """
        returns area of square -> (float)
        """
        if self.square_side > 0:
            a = self.square_side
            s = a*a
            return float(s)
        else:
            return 0
    
    def perimeter(self):
        """
        returns peremets of square -> (float)
        """

        if self.square_side > 0:
            a = self.square_side
            p = a * 4
            return float(p)

        else:
            return 0
