# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def factorial(inp):
    inp = int(inp)
    total = 1
    for n in range(1, inp + 1):
        total *= n
    return total


def digit_sum(inp):
    total = 0
    inp = str(inp)
    for digit in range(len(inp)):
        total += int(inp[digit])
    return total



 print(digit_sum(factorial(100)))
    