import math
from functools import reduce

def factors(n, limit):    
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1,limit+ 1) if n % i == 0)))

def FUNC(num):
  returns = [8234214342]
  for i in range(100000001,num+1):
    if i % 100 == 0:
        print(str(i) + " : " + str(sum(returns)))
    returns.append(getDiv(i))
  return sum(returns)

def getDiv(num):
  divs = []
  numB = 2 * (num * num)
  factorsNum = factors(numB, num)
  factorsNew = []
  factorsNum.sort()
  for factor in factorsNum:
    if (factor <= num):
      factorsNew.append(factor)
    else:
        break
  ans = len(factorsNew)
  return(ans)

print(FUNC(10**12))