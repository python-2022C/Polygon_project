import math

class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(s,a,b,c):
        if s.a + s.b > s.c and s.a + s.c > s.b and s.b + s.c > s.a:
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

# Create method "area" in the Triangle class
# This method finds the area of the triangle
# return area of the triangle if the triangle is valid, 0 otherwise
