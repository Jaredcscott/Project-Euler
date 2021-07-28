'''
    @author Jared Scott
    Prob 27 of Project Euler Solved 7/28/21
    Run Time: 0:05 
'''
import math 
import time

def isPrime(num):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
        
        Arguments: 
            (Integer) num: The number which you would like to test
            
        Output:
            True if the number is prime, or False if the number is not prime 
    '''
    if num < 0:
        num = -1 * num
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False
        
        
def solve(limit,a,b):
    #Implements n^2 + an + b
    primes = []
    for n in range(limit+1):
        term1 = n * n 
        term2 = a * n 
        val = term1 + term2 + b
        if isPrime(val):
            primes.append(val)
        else:
            break 
    return len(primes)
    
def find(n):
    most = 0
    mostN = 0
    ab = ()
    limA = 1000
    limB = 1000
    for a in range(-1*(limA),limA):
        for b in range(-1*(limB),limB):
            len = solve(n,a,b)
            if len > most:
                most = len
                ab = (a,b)
                print("New Most Found!\nmost: " + str(most) + " n: " + str(n) + " a: " + str(a) + " b: " + str(b))
    print(mostN,most,ab)
    
start_time = time.time()
find(100)
seconds = time.time() - start_time
minutes = 0 
while seconds > 60:
    minutes += 1
    seconds -= 60
print("Runtime: " + str(minutes) + ":" + (str(int(seconds)) if seconds>9 else "0"+ str(int(seconds))))   
    
 
