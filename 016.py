# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


num = 2 ** 1000
num = str(num)
length = len(num)
sum = 0
x = 0
for i in range(length):
    x = int(num[i])
    sum += x

print(sum)