from triangleNums import triangleNums
'''
for i in range(1,50000):
    curNum = 0
    for j in range(1,i+1):
        curNum += j
    triangleNums.append(curNum)



print(triangleNums)

'''
#print(triangleNums)
highestNum = 0
highestFactors = 0
for triNum in triangleNums:
    factors = []
    #while len(factors) <= 500:
    for i in range(1,triNum//2 + 1):
        if triNum % i == 0 and i not in factors:
            factors.append(i)
    factors.append(triNum)
    if len(factors) > highestFactors:
        highestFactors = len(factors)
        print(triNum)
        print(factors)
        print("factors: " + str(highestFactors))
    if len(factors) > 500:
        highestNum = triNum
        break


print(highestNum)



                
