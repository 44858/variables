#Lewis Travers
#19/09/2014
#Currency

money1 = int(input("Please enter a whole amount of money"))

answer20 = money1 // 20
money2 = money1 % 20

answer10 = money2 // 10
money3 = money2 % 10

answer5 = money3 // 5
money4 = money3 % 5

answer2 = money4 // 2
money5 = money4 % 2

answer1 = money5

print("The minimum amount of £20 notes needed is {0}, of £10 notes is {1}, of £5 notes is {2}, of £2 coins is {3}, of £1 coins is {4} ".format(answer20, answer10, answer5, answer2, answer1))
