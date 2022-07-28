import math
class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        return self.radius > 0
    
    def diameter(self):
        '''
        This method finds the diameter of the circle.

        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid():
            return 2 * self.radius
        return 0
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.

        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid():
            return 2 * math.pi * self.radius
        return 0
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.

        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid():
            return math.pi * self.radius**2
        return 0


    def diameter(self):
        if self.r > 0:
            return self.r*2
        else:
            return 0

    def circumference(self):
        if self.is_valid():
            return 2*math.pi*self.r
        else:
            return 0

    def area(self):
        if self.is_valid():
            return 2*math.pi*self.r**2
        else:
            return 0


