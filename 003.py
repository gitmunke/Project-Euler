# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

inp = input('check for prime ')
num = int(inp)


def is_prime(num):
    start = 2
    lpg = int(math.sqrt(num))
    while start <= lpg:
        if num % start == 0:
            print(start, 'is a factor')
            return False        
        start = start + 1
    print(num, 'is prime')
    return True

print(is_prime(num))