# Q6 The sum of the squares of the first ten natural numbers is 385.
# The square of the sum of the first ten natural numbers is 3025.
# Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum
# is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

oneToHundred = list(range(1,101))
sumOfSquares = sum([i**2 for i in oneToHundred])

squareOfTheSum = (sum(oneToHundred))**2

answer = squareOfTheSum - sumOfSquares
print(answer)