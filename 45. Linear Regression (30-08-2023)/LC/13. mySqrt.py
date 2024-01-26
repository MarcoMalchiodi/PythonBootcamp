def mySqrt(x): # numbers rounded up to the lowest value
    
    if x == 1 or x == 0:
        return print(x)
    
    for n in range(1000):
        if (n*n == x):
            return print(n)
        elif (n*n > x):
            return print(n-1)

mySqrt(271)