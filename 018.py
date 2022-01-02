#
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
# Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)


str_triangle = \
     """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


triangle = []

rows = str_triangle.split('\n')

for c in rows:
    triangle.append([int(num) for num in c.split(' ')])

sum = 0
x = 0

def whole_number(num):
    if num < 0:
        return 0
    else:
        return num

    
for x in range(len(triangle)):
    for y in range(len(triangle[0])):
        sum += triangle[x][y]
        print(sum)

for x in range(len(triangle)):
    sum = 0
   
    for x in range(len(triangle)):
        for y in range(len(triangle[0])):
            sum += triangle[x][y]
            print(sum)

#first loop 2nd index is [0], for next loop 2nd index is [0] until first index is [14], maybe i could make something that if you give it a negative value it returns zero
#i think this loop will give me the right value for 2nd index, but it continues to go up, maybe i can use another loop w/ if statement, if whole num > loop count wholenum = loop count

for c in range(len(triangle)):
    for x in range(len(triangle)):
        pos = whole_number(x - len(triangle) + c + 1)
        print(whole_number(x - len(triangle) + c + 1))
        if pos > c:
            pos = c
        print(pos)

#ill try a third loop

for z in range(len(triangle)):
    for c in range(len(triangle)):
        
        for x in range(len(triangle)):
            pos = whole_number(x - len(triangle) + c + 1)
            if pos > z:
                pos = z
            print(pos)



#i think its calcing some things twice, but this should work for detrmining the 2nd index value
cum_sum = 0
largest = 0
for z in range(len(triangle)):
    for c in range(len(triangle)):
        if cum_sum > largest:
            largest = cum_sum
        cum_sum = 0
        for x in range(len(triangle)):
            pos = whole_number(x - len(triangle) + c + 1)
            if pos > z:
                pos = z
            cum_sum += triangle[x][pos]
            print(cum_sum, pos)
print(largest)

