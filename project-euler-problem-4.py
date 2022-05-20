# Q4 A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Finding all the products of 2 3-digit numbers.
multipliedList = []
extendedMultipliedList = []
numbers = list(range(100,1000))
for n in range(100,1000):
    multipliedList.append([i * n for i in numbers])
    extendedMultipliedList = [x for l in multipliedList for x in l]

# Finding all the palindromic numbers in that list.
palindromicMultipliedList = []
for q in extendedMultipliedList:
    if int(str(q)[::-1]) == q:
        palindromicMultipliedList.append(q)

# Finding and printing the maximum palindromic number.
maxPalindromicMultiple = max(palindromicMultipliedList)
print(maxPalindromicMultiple)