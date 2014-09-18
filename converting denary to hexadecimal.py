#Lewis Travers
#18/09/2014
#Converting denary to hexadecimal

denary_value = int(input("Please enter a denary number: "))
binary_string = ""
while denary_value > 0:
    binary_string = str(denary_value%2) + binary_string
    denary_value = denary_value // 2
print("The binary equivalent is {0}".format(binary_string))
