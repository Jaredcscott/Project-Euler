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




def sumFactors(factors):
    sum = 0
    for j in curfactors:
        if j * j == 284:
            continue
        else:
            sum += j
    return sum
          
for i in range(10000):
    curfactors = print_factors(i)
    otherNum = sumFactors(curfactors)
    otherFactors = print_factors(otherNum)
    otherSum = sumFactors(otherNum)
    if sumFactors(curfactors) ==  otherSum:
        print('amicable', sumFactors(curfactors), otherSum) 
        

      