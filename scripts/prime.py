import sys, math

def prime(a):
    sqtofA = int(math.sqrt(a))
    for i in range(1, sqtofA):
        if a%i == 0:
            return False
    
    return True
    
pn = int(sys.argv[1])
print(prime(pn))