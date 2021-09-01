from math import *
def Check(N):
    
    for i in range(1, int(sqrt(N)) + 1): #checking number from 1 to sqrt(N)
        square = i*i                     #saving square of number
        diff = N - square                #subtracting square from given N

        sqrtdiff = int(sqrt(diff))       #checking if diff is perfect square

        if sqrtdiff * sqrtdiff == diff :
            return True
    return False

print(Check(4))