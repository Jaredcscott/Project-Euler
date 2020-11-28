def print_factors(x):
    # This function takes a number and prints the factors
    factors = []
    #print("The factors of",x,"are:")
    for i in range(1, x):
       if x % i == 0:
           factors.append(i)
    return factors
sum = 0

def sumFactors(factors, num):
    sum = 0
    for j in factors:
        if j * j == num:
            continue
        else:
            sum += j
    return sum
          
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