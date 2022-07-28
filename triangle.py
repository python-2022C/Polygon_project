import math

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a=a 
        self.b=b
        self.c=c

        # Create method "is_valid" in the Triangle class
        # This method checks if the triangle is valid
        # True if the triangle is valid, False otherwise

        # Create method "get_type" in the Triangle class
        # This method finds the type of the triangle

        # Create method "perimeter" in the Triangle class
        # This method finds the perimeter of the triangle
        # return perimeter of the triangle if the triangle is valid, 0 otherwise

        # Create method "area" in the Triangle class
        # This method finds the area of the triangle
        # return area of the triangle if the triangle is valid, 0 otherwise

    def is_valid(self):
        l=self.a+self.b+self.c-max(self.a,self.b,self.c)-min(self.a,self.b,self.c)
        if max(self.a,self.b,self.c)+min(self.a,self.b,self.c) > l :
            return True
        else:
            return False
    def get_type(self):
        if self.c**2 == self.a**2 + self.b**2:
            return 'right angle'
        elif self.b == self.c:
            return 'equilateral'
        elif self.c**2 == self.a**2 == self.b**2:
            return "equal side"
        