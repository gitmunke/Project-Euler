# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math
import utilities
#inp = input('check for prime ')
#num = int(inp)

largest = 0

for x in range(1, 775146):
    if 600851475143 % x == 0:
        if utilities.is_prime(x) == True:
            if x > largest:
                largest = x


print(largest)