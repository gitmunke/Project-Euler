

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for x in range(2, num):
        if x * x > num:
            break
        if num % x == 0:
            return False
     
    return True