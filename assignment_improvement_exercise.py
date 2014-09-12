#john bain
#variable improvement exercise
#05-09-12

import math

circle_radius = float(input("please enter the radius of the circle: "))

circle_circumference = 2* math.pi * circle_radius
circle_circumference = round(circle_circumference,2)

circle_area = math.pi * circle_radius**2
circle_area = round(circle_area,2)

print("The circumference of this circle is {0}.".format(circle_circumference))
print("The area of this circle is {0}.".format(circle_area))
