import math

def is_perfect_root(b):
    if(b >= 0):
        sr = math.sqrt(b)
        return ((sr*sr) == float(b))
    return False

def find_true(c):
    for i in range(1,int(math.sqrt(c)))):
        b = c - i*i 
        if is_perfect_root(b) and b > 0:
            return True
    return False


print(find_true(3))
