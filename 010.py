# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

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

sum = 2
for n in range(3, 2000000, 2): #inc 2 because all primes besides 2 are odd
   if is_prime(n) == True:
        sum += n
print(sum)