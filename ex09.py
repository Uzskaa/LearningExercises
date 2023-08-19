# Title: Area of the Circle
# This program calculates the area of a circle based on the radius entered by the user.
import math

radius = int(input('Enter Radius: '))
area = math.pi * (radius**2)

print("Radius:", radius)
print("Area of the Circle:",area)