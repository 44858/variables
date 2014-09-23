#Lewis Travers
#23/09/2014
#calculating volume of a pool

width = int(input("Please enter the width of the pool: "))
length = int(input("Please enter the length of the pool: "))
depth = int(input("Please enter the depth of the pool: "))
main_volume = length * width * depth
circle_radius = width / 2
circle_area = 3.14 * (circle_radius * circle_radius)
half_circle_volume = (circle_area / 2) * depth
pool_volume = main_volume + half_circle_volume
print("The total volume of the pool is approximately {0}.".format(pool_volume))
