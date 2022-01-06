# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
# circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200] # maybe i should start with the 2 pound coin, [7]

coins_temp = []
max_value = 200
different_ways = 0


for coin_range in range(7, -1, -1):
    temp_total += coins[coin_range]
    



def coin_counter(coin_value, max_value):
