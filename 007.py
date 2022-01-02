# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for x in range(2, num):
        if x * x > num:
            break
        if num % x == 0:
            return False
     
    return True

start = 2
primes = []
while len(primes) < 10001:
    if is_prime(start) == True:
        primes.append(start)
    start += 1
        
print(primes[-1])
