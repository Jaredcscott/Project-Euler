import time

primes = []
count = 0 
while len(primes) <= 10015:
    factors = []
    for i in range(count + 1):
        factors = []
        for j in range(1,i//2):
            if i % j == 0:
                #print("Factors Found!! nums :", end="")
                #print(i,end='')
                #print(',',end='')
                #print(j)
                factors.append(j)
                factors.append(i)
                if len(factors) > 2:
                    break
        if len(factors) == 2 and i not in primes:
            primes.append(i)
            print()
            if len(primes) > 5000:
                if len(primes) % 200 == 0:
                    print("prime found!!")
                    print(primes[-15:-1])
                    print('----------------------------------------------------------------------------------------------') 
                    time.sleep(.2)
                    print()
                    
            elif len(primes) > 200 and len(primes) % 20 == 0:
                    print("prime found!!")
                    print(primes[-15:-1])
                    print('----------------------------------------------------------------------------------------------') 
                    #time.sleep(1)
                    print()        
            continue
    count += 1 
for i in primes:
    print(i)
print(len(primes))
print("^^Your number^^")
print(str(count) + "count")
