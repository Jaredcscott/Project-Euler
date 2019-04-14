import math

primeSum = 0
for num in range (2,2000000):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        primeSum += num
        print(str(num) + " Current sum: " + str(primeSum))

print(primeSum)

#for i in primes:
#    print(i)

'''for i in primes:
    print(i)
print(len(primes))
print("^^Your number^^")i
print(str(count) + "count")
'''

