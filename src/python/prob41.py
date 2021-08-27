import math 

#@author Jared Scott

def getPrimes(n):
    #Implements the sieve of eratosthenes 
    print("Generating prime numbers smaller than: ",n)
    primes = [True for i in range(n+1)]
    primes[0] = primes[1] = False
    primeIndex = 2
    #Running a loop to check all numbers below the square root of the given number
    while primeIndex ** 2 < n:
        if primes[primeIndex]:
            for number in range(primeIndex*2, n+1, primeIndex):
                primes[number] = False
        #Increment the starting number by one to keep the loop working
        primeIndex += 1    
    prime_numbers = [i for i in range (n+1) if primes[i]==True]
    print("Generation finished","\nNumber of primes found: ",len(prime_numbers))
    return prime_numbers

def isPanDigital(num):
    nums = []
    duplicateNums = False
    numStr = str(num)
    numLen = len(numStr)
    for char in numStr:
        if char in nums:
            return False
        else:
            nums.append(char) 
    nums.sort()   
    if nums[0] != '0' and len(nums) == numLen:
        comp = 1
        for val in nums:
            if int(val) == comp:
                comp += 1
            else: 
                return False 
        return True 
    
primes = getPrimes(10000000)
largest = 0
for prime in primes:
    if isPanDigital(prime):
        if prime > largest:
            largest = prime
            
print("New Largest Found: ",largest)
