# Introduction to Polygon
Polygon are two-dimensional geometric objects composed of points and straight lines connecting those points.

Sample of Polygon:

![polygon](https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/277097a6a870457e90553ed24cf46042/1548051233_Two-dimensional-2-D-shapes-circle-triangle-square-polygons.png
)

## Type of Polygon:
1. Triangle
2. Rectangle
3. Square
4. Circle

## Notation of triangle

![triangle](https://i.stack.imgur.com/1GkR3.png
)

## Properties of Square

1. Distance
2. Side
3. Perimeter
4. Area

## Properties of Rectangle

1. Distance
2. Side
3. Perimeter
4. Area

## Properties of Triangle

1. Distance
2. Side
3. Perimeter
4. Area

## Properties of Circle

1. Diameter
2. circumference
3. Area

# Usage examples

## Example of Square

```python
square_points = [(0,0), (0,4), (4,4), (4,0)]
square = Square(square_points)
square_sides = square.sides()
square_perimeter = square.perimeter()
square_area = square.area()

print("The sides of the square are:", square_sides)
# The sides of the square are: [4.0, 4.0, 4.0, 4.0]
print("The perimeter of the square is:", square_perimeter)
# The perimeter of the square is: 16.0
print("The area of the square is:", square_area)
# The area of the square is: 16.0
```

## Example of Rectangle

```python
rectangle = Rectangle([(0,0), (3,0), (3,4), (0,4)])
rectangle_sides = rectangle.sides()
rectangle_perimeter = rectangle.perimeter()
rectangle_area = rectangle.area()

print("The sides of the rectangle are:", rectangle_sides)
# The sides of the rectangle are: [4.0, 3.0, 4.0, 3.0]
print("The perimeter of the rectangle is:", rectangle_perimeter)
# The perimeter of the rectangle is: 14.0
print("The area of the rectangle is:", rectangle_area)
# The area of the rectangle is: 12.0
```

## Example of Triangle

```python
triangle = Triangle([(1,1), (4,3), (6,1)])
triangle_sides = triangle.sides()
triangle_perimeter = triangle.perimeter()
triangle_area = triangle.area()
print("The sides of the triangle are:", triangle_sides)
# The sides of the triangle are: [5.0, 3.605551275463989, 2.8284271247461903]
print("The perimeter of the triangle is:", triangle_perimeter)
# The perimeter of the triangle is: 11.43397840021018
print("The area of the triangle is:", triangle_area)
# The area of the triangle is: 5.0
```

## Example of Circle

```python
circle = Circle(5)
circle_diameter = circle.diameter()
circle_circumference = circle.circumference()
circle_area = circle.area()
print("The diameter of the circle is:", circle_diameter)
# The diameter of the circle is: 10
print("The circumference of the circle is:", circle_circumference)
# The circumference of the circle is: 31.41592653589793
print("The area of the circle is:", circle_area)
# The area of the circle is: 78.53981633974483
```