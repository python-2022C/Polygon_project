import math

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a=a 
        self.b=b
        self.c=c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.

        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        min_side = min(self.a, self.b, self.c)
        max_side = max(self.a, self.b, self.c)
        middle_side = self.a, self.b, self.c - max_side - min_side
        return middle_side < min_side + max_side
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        '''
        if self.is_valid():
            if self.a == self.b and self.b == self.c: 
                return "By Side: Equilateral Triangle"
            elif self.a == self.b or self.a == self.c or self.b == self.c: 
                return "By Side: Isoceles Triangle"
            else:
                return "By Side: Scalene Triangle"
        else:
            return "this triangle is not valid"
        
    def perimeter(self):
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            return self.a + self.b + self.c
        return 0

    def area(self):
        '''
        This method finds the area of the triangle.

        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            semi_petemeter = self.perimeter() / 2
            s = math.sqrt(semi_petemeter * (semi_petemeter - self.a) * (semi_petemeter - self.b) * (semi_petemeter - self.c))
            return s
        else:
            return 0
