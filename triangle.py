import math

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a=a 
        self.b=b
        self.c=c
    def is_valid(a,b,c):
        l=a+b+c-max(a,b,c)-min(a,b,c)
        if max(a,b,c)+min(a,b,c)>l :
            return True
        return False
    


# Create method "is_valid" in the Triangle class
# This method checks if the triangle is valid
# True if the triangle is valid, False otherwise

# Create method "get_type" in the Triangle class
# This method finds the type of the triangle

# Create method "perimeter" in the Triangle class
# This method finds the perimeter of the triangle
# return perimeter of the triangle if the triangle is valid, 0 otherwise
    def perimeter(self) :
        return self.a+self.b+self.c


# Create method "area" in the Triangle class
# This method finds the area of the triangle
# return area of the triangle if the triangle is valid, 0 otherwise
