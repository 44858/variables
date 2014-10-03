#Lewis Travers
#16/09/2014
#DIVMOD

number1 = int(input("Please enter an integer: "))
number2 = int(input("Please enter an intger for the first to be divided by: "))

answer = number1 // number2
remainder = number1 % number2

print("The answer is {0} and the remainder is {1} ".format(answer, remainder))
