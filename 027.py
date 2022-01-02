# Euler discovered the remarkable quadratic formula:
#
# n^2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,
# 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41
#
# is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
#
# . The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n^2+an+b
#
# , where |a|<1000 and |b|≤1000
#
# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n=0.


# one for loop for a and one for b, starting from 1000 for a and only using primes for b

def is_prime(num):
    if num < 2:
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


inc_negative = []
for i in range(1, 1001):
    if is_prime(i) == True:
        
        inc_negative.append(i)
        inc_negative.append(-i)

val_a = 0
val_b = 0
greatest = 0


for a in inc_negative:
    for b in inc_negative:
        n = 0
        while is_prime((n ** 2) + (a * n) + b) == True:
            n += 1
            if n > greatest:
                greatest = n
                val_a = a
                val_b = b
print(greatest)
print(val_a, val_b)
print(val_a * val_b)


