import math

def is_perfect_root(b):
        sqr = math.sqrt(b)
        if((sqr*sqr) == float(b)):
            return True
        else:
            return False

def find_true(c):
    for i in range(1,int(math.sqrt(c))):
        b = c - i*i 
        if is_perfect_root(b) and b > 0:
            return True
    return False


print(find_true(5))
