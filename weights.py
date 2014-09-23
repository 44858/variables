#Lewis Travers
#23/09/2014
#Weights

weight = int(input("Please enter a weight in whole grams: "))

weights100 = weight//100
remainder1 = weight%100

weights50 = remainder1//50
remainder2 = remainder1%50

weights10 = remainder2//10
remainder3 = remainder2%10

weights5 = remainder3//5
remainder4 = remainder3%5

weights2 = remainder4//2
remainder5 = remainder4%2

weights1 = remainder5


print("You will need {0} 100g weights, {1} 50g weights, {2} 10g weights, {3} 5g weights, {4} 2g weights and {5} 1g weights.".format(weights100, weights50, weights10, weights5, weights2, weights1))
