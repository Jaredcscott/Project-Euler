'''
    @Author Jared Scott ☯
    This will take a VERY long time with large inputs ( > 30 hrs) 
    I solved this problem by performing the calculation in pieces over 7 days 
    Execution can be broken into chunks by changing the lower bound of the 
    range function on line 38 to a reached iteration. Then adding the cumulative 
    sum into the "returns" list on line 37. 
    See comment in Function for milestone values
'''
import math
from functools import reduce

def factors(n, limit):  
    '''
    Found the reduce function here: https://stackoverflow.com/questions/6800193
    Inner comprehension produces a tuple filled with the factor pairs found using the modulus operation
    Reduce function will apply the given function (in this case it is adding the factor lists) and discards duplicate entries
    '''
    return list(reduce(list.__add__,([i, n//i] for i in range(1,limit+ 1) if n % i == 0)))

def getDiv(num):
  #This function will return a list of divisors of 2*(num^2) which are smaller or equal to num
  divs = []
  numB = 2 * (num * num)
  factorsNum = factors(numB, num)
  factorsNum.sort()
  factorsNew = []
  for factor in factorsNum:
    if (factor <= num):
      factorsNew.append(factor)
    else:
        break
  return(len(factorsNew))

def Function(num):
  #Milestone values: 100000:3552444, 100000001:8234214342
  print(("-"*15) + "\nSolving for: " + str(num) + "\nSeed:Sum Value")
  returns = []
  for i in range(1,num+1):
    if i % 400 == 0:
        print(str(i) + " : " + str(sum(returns)))
    returns.append(getDiv(i))
  return sum(returns)

def main():
    print("Solution for 15: " + str(Function(15)))
    print("Solution for 1000: " + str(Function(1000))) 
    print("Solution for 10^12: " + str(Function(10**12)))
    
if __name__ == "__main__":
    main()
