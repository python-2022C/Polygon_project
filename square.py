import math

class Square:
    def __init__(self, square_side:float):
        """
        is_valid() -> bool
        area() -> float
        perimeter() -> float
        """
        self.square_side = square_side
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.

        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """        
        return self.square_side > 0
    
    def area(self):
        """
        This method finds the area of the square.

        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        if self.is_valid(): 
            return self.square_side * self.square_side
        return 0
    
    def perimeter(self):
        """
        This method finds the perimeter of the square.

        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        if self.is_valid():
            return self.square_side * 4
        return 0
