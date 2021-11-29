'''
    @Author Jared Scott ☯
    This script will solve the 46th problem for Project Euler 
    
'''
import math

def isPrime(num):
    #This function determines if the provided number is prime or not by doing a remainder calculation on all potential roots less than 1 + sqrt(val) 
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False
        
def getLesserPrimes(num):
    nums = []
    for val in range(num):
        if (isPrime(val)):
            nums.append(val)
    return nums 

def generateOddCompositeNums(limit):
    # This function will generate a list of all composite numbers from 1 until the limit provided 
    # Uses prime factor calculation 
    nums = []
    for val in range(limit+1):
        if (not isPrime(val)) and val % 2 != 0:
            nums.append(val)
    return nums
    
def testEquality(val,prime,root):
    if (val == (prime + (2 * (root * root)))):
        
        return True
    else:
        return False
    
def main():
    compNums = generateOddCompositeNums(10000)
    count = 0
    for num in compNums:
        count += 1
        found = False
        lesserPrimes = getLesserPrimes(num)
        for prime in lesserPrimes:
            for root in range(num):
                if testEquality(num,prime,root):
                    if (count % 150 == 0):
                        print("Equality found!: " + str(num) + "=" + str(prime) + " + 2*" + str(root)+ "^2")
                    found = True 
                    continue
        if not found:
            print("----------------------Answer not found: " + str(num))
        
    
if __name__ == '__main__':
    main()
    
