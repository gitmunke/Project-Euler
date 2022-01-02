# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
#
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025−385=2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#square of sum
sum = 0
for s1 in range(1, 101):
    sum = s1 + sum
sos1 = sum ** 2
print(sos1)

#sum of square
sq = 0
for s2 in range(1, 101):
    sq = s2 ** 2 + sq
print(sq)

#difference
final = sos1 - sq
print(final)

#functions
def square_of_sum(max):
    sum = 0
    for s1 in range(1, max + 1):
        sum += s1
    sqos = sum ** 2
    print(sqos)
    return sqos

def sum_of_square(max):
    sum = 0 
    for s2 in range(1, max + 1):
        sum += s2 ** 2
    print(sum)
    return sum

pb = square_of_sum(100)
j = sum_of_square(100)
final2 = pb - j
print(final2)