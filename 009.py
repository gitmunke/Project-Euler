# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for c in range(900, 1, -1):
    for b in range(c - 1, 2, -1):
        if b + c <= 999:
            a = 1000 - b -c
            if a < b < c:
                if a ** 2 + b ** 2 == c ** 2:
                    print(a, b, c)
                    print(a * b * c)