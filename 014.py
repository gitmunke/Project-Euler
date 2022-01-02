# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

#even or odd function
def is_even(num):
    return num % 2 == 0

#collatz even and odd
def col_even(num):
    return num / 2

def col_odd(num):
    return num * 3 + 1

start = 1
starting_num = 1
longest = 1
terms = 1

for num in range(2, 1000000):
    terms = 1
    start = num
    while num != 1:
        if is_even(num):
            num = col_even(num)
            terms += 1
        else:
            num = col_odd(num)
            terms += 1
    if terms >= longest:
        longest = terms
        starting_num = start
        print(starting_num, 'produces the longest chain ', longest)
print(starting_num, 'produces the longest chain ', longest)