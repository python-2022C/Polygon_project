
class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b


    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        return self.a > 0 and self.b > 0


    def perimeter(self):
        """
        This method finds the perimeter of the rectangle.

        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        return (self.a*2) + (self.b*2) if self.is_valid() else 0


    def area(self):
        """
        This method finds the area of the rectangle.

        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        return float(self.a * self.b) if self.is_valid() else 0
