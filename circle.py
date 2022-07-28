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
        r = self.radius
        return r > 0


    def diameter(self):
        '''
        This method finds the diameter of the circle.

        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid():
            r = self.radius
            d = 2 * r
            return d

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
            r = self.radius
            d = 2 * r
            pi =  math.pi
            return d * pi

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
            pi = math.pi
            r = self.radius
            s = r**2*pi
            return s

        return 0


