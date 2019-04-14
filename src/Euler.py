def isPrime(num):
        factors = []
        for i in range(int(num + 1/2)):
            for j in range(num + 1):
                if i * j == num:
                    if i not in factors:
                        factors.append(i)
                    if j not in factors:
                        factors.append(j)
                        if len(factors) > 2:
                            continue
        print(num," trying a factor")
        if len(factors) == 2:
            return True
        else:
            return False
        
num = []
largestFactor = 1
for i in range(1,int(600851475143/2)):
    if 600851475143 % i == 0:
        if isPrime(i):
            num.append(i)
            print(num)
print("done")
