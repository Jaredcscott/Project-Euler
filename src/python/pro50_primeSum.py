import math
def isPrime(num):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
        
        Arguments: 
            (Integer) num: The number which you would like to test
            
        Output:
            True if the number is prime, or False if the number is not prime 
    '''
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False

def findNum(limit):
    primes = []
    curNum = 2
    while curNum < limit:
        if (isPrime(curNum)):
            primes.append(curNum)
        curNum += 1
    longestSumLength = 0
    curLongestSum = 0
    startIndex = 0
    while startIndex < len(primes)-1:
        length = 2
        while length < len(primes)-1 - startIndex:
            curSum = 0
            curSum += primes[startIndex]
            termCount = 1
            while termCount <= length:
                curSum += primes[startIndex+termCount]
                termCount += 1
            if isPrime(curSum):
                if length > longestSumLength and curSum < limit:
                    curLongestSum = curSum
                    longestSumLength = length
                    print("Prime Sum Found: " + str(curSum) + " Terms: " + str(length))
                
            length += 1
            if (length % 5 == 0):
                print("Terms: " + str(length))
        startIndex += 1
    print(str(primes))

def main():
    findNum(1000000)

main()
