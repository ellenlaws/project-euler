# Q5 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# this is my first attempt - just a brute force method to get me thinking
# numbers = list(range(1,1000000000))
# numbers_2 = list(range(1,21))
# answer = []
#
# for n in numbers:
#     if n % 1 == 0:
#         if n % 2 == 0:
#             if n % 3 == 0:
#                 if n % 4 == 0:
#                     if n % 5 == 0:
#                         if n % 6 == 0:
#                             if n % 7 == 0:
#                                 if n % 8 == 0:
#                                     if n % 9 == 0:
#                                         if n % 10 == 0:
#                                             if n % 11 == 0:
#                                                 if n % 12 == 0:
#                                                     if n % 13 == 0:
#                                                         if n % 14 == 0:
#                                                             if n % 15 == 0:
#                                                                 if n % 16 == 0:
#                                                                     if n % 17 == 0:
#                                                                         if n % 18 == 0:
#                                                                             if n % 19 == 0:
#                                                                                 if n % 20 == 0:
#                                                                                     answer.append(n)
#                                                                                     break
#
# print(answer)

# my second attempt, I am happy with this solution
oneToTwentyList = list(range(1,21))
solution = []

for n in range(2520,10000000000,2520):
    if all(n % i == 0 for i in oneToTwentyList):
        solution.append(n)
minSolution = min(solution)
print(minSolution)