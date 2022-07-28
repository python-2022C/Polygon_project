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
        return self.square_side > 0

    def area(self)-> bool:
        """
        returns area of square -> (float)
        """
        if self.square_side > 0:
            return float(self.square_side * self.square_side)
        else:
            return 0
    
    def perimeter(self):
        """
        returns peremets of square -> (float)
        """

        if self.square_side > 0:
            return float(self.square_side * 4)

        else:
            return 0
