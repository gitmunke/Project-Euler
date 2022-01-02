
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


#potential range
#100 * 100 = 10000
#999 * 999 = 998001

#1. find palindromes starting from 998001       997799   generate palindromes from 3 digit factors
#2. find 3 digit factors of palindromes (100 - 999)

#some_string = 'hello'
#print(some_string[0])  # h
#print(some_string[-1])  # o

#array = [1, 2, 3]
#string = 'hello'
#array[0]  # 1
#string[0]  # 'h

#num_iterations = len(str_num) // 2
#for i in range(num_iterations):
#  if str_num[i] != str_num[-1 - i]:
#    return False
#return True

#for i in range(999, 99, -1):
#  for j in range(999, 99, -1):
#    number_with_three_digit_factors = i * j

def is_palindrome(num):
    num = str(num)
    if num[0] == num[-1]:
        if num[1] == num[-2]:
            if num[2] == num[-3]:
                print(num, 'is palindrome')
                return True
    else:
        #print('not a palindrome')
        return False


for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        final = i * j
        if is_palindrome(final) == True:
             print(final)