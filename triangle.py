import math
class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        if self.a+self.b>self.c and self.a+self.c>self.b and  self.b+self.c>self.a :
            return True
        return False
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.
        '''
        if self.a==self.b==self.c :
            return "Teng tomonli"
        elif self.a==self.b or self.b==self.c or self.a==self.c :
            return "Teng yonli"
        elif self.a!=self.b and self.b!=self.c and self.a!=self.c:
            return "Turlli tomonli"
        return "TUg'ri burchakli"
        
    def perimeter(self):
        '''
        This method finds the perimeter of the triangle.

        Args:
            No
        Returns:
            int or float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
            return self.a + self.b + self.c
    def area(self):
        '''
        This method finds the area of the triangle.
        
        Args:
            NO
        Returns:
            int or float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        x=max(self.a,self.b,self.c)
        y=min(self.a,self.b,self.c)
        z=self.a+self.b+self.c-x-y
        if pow(z,2)+pow(y,2)==pow(x,2):
            return (z*y)/2
        return 0
