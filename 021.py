# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def sum_proper_divisors(inp):
    inp = int(inp)
    final = []
    for div in range(1, inp // 2 + 1):
        if inp % div == 0:
            final.append(div)
    return sum(final)


stor = []

for inp in range(1, 10000):
    if inp in stor:
        continue
    pair = sum_proper_divisors(inp)
    if sum_proper_divisors(pair) == inp:
        if inp != pair:
            stor.append(inp)
            stor.append(pair)
            print(inp, pair)

print(sum(stor))