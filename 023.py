# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sum_proper_divisors(inp):
    inp = int(inp)
    final = []
    for div in range(1, inp // 2 + 1):
        if inp % div == 0:
            final.append(div)
    return sum(final)


abundant = []

for x in range(1, 28123):
    if sum_proper_divisors(x) > x:
        abundant.append(x)

sum_of_two_abundant = []

def sum_of_abundant(x):
    if x < 24:
        return False
    for n in range(x):
        if x - abundant[n] in abundant:
            return True
        if abundant[n] > x:
            return False

not_sum = []

for x in range(1,28123):
    if sum_of_abundant(x) == False:
        not_sum.append(x)

print(sum(not_sum))
