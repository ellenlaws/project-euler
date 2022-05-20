# Q7 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


numbers = list(range(2,1000000))
primes = []

for i in numbers:
    if all(i % x != 0 for x in range(2, i)):
        primes.append(i)

nthPrime = primes[10000]

print(nthPrime)