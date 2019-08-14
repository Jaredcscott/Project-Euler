def print_factors(x):
    # This function takes a number and prints the factors
    factors = []
    #print("The factors of",x,"are:")
    for i in range(1, x):
       if x % i == 0:
           factors.append(i)
    return factors
sum = 0
#for i in range(1,10):
#    curfactors = print_factors(i)
#    for j in curfactors:
#        if j * j == i:
#            continue
#        else:
#                sum += j

#print(sum)




def sumFactors(factors, num):
    sum = 0
    for j in factors:
        if j * j == num:
            continue
        else:
            sum += j
    return sum
          
#for i in range(285):
#    curFactors = print_factors(i)
#    print(sumFactors(curFactors, i),' ', i)
    
    #otherNum = sumFactors(curfactors)
    #otherFactors = print_factors(otherNum)
    #otherSum = sumFactors(otherNum)
    #if sumFactors(curfactors) ==  otherSum:
    #    print('amicable', sumFactors(curfactors), otherSum) 
        
#curFactors = print_factors(284)
#print(sumFactors(curFactors, 284),' ', 284) # 220 284 
#curFactors1 = print_factors(220)
#print(sumFactors(curFactors1, 220), ' ', 220) # 284 220
#if sumFactors(curFactors1, 220) == 284 and sumFactors(curFactors, 284) == 220:
#            print("here")
sum = 0
for i in range(1,10001):
    curFactors = print_factors(i)
    for j in range(i + 1):
        curFactors1 = print_factors(j)
        if sumFactors(curFactors1, j) == i and sumFactors(curFactors, i) == j and sumFactors(curFactors, i) != i:
            sum += i
            sum += j
            print(i, ' ',j)
            print("current sum: ", sum)

print(sum)      