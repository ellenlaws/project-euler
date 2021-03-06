# Q1 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
numbers = list(range(1,1000))
multiples3and5 = numbers[2::3] + numbers[4::5]
for i in multiples3and5:
    if i in multiples3and5[multiples3and5.index(i)+1:]:
        multiples3and5.remove(i)

sumOfMultiples = sum(multiples3and5)
print(sumOfMultiples)