import math

def computeQuadratic(a,b,n):
    result = (n ** 2) + (a * n) + b
    print(result)
    return result

def isPrime(num):
    #print(type(num))
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False

maxdist = 0
maxConfig = []
for a in range(-999,1000):
    for b in range(-1000,1001):
        for n in range(1,1000):
            curDist = 0
            result = computeQuadratic(a,b,n)
            if result < 0:
                result *= -1
            while isPrime(result):
                curDist += 1
            if curDist > maxdist:
                maxdist = curDist
                maxConfig[0] = a
                maxConfig[1] = b
                maxConfig[2] = c
                
print(maxdist)
print(maxConfig)

