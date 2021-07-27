limit = 1000
    
def countCycleLen(number,printRem):
    '''
        Iteratively permute the remainder until 
        the remainder of the current iteration is the same 
        as the last iteration. 
        IE divide a shifted value by a number until either no remainder is left, or a cycle is found
    '''
    remainder = []
    shiftRem = [10]
    cycling = True
    while cycling:
        if ((shiftRem[-1]) % number)*10 in shiftRem:
            #A cycle has been completed IE the permutation has already been recorded
            break
        shiftRem.append((shiftRem[-1] % number)*10) #Adding in shifted remainder 
        remainder.append(int(str((shiftRem[-2] / 10)/number)[2])) #Adding in char to remainder list
    remainder.append(int(str((shiftRem[-1] / 10)/number)[2]))  
    if printRem:
        print(remainder)
    return len(shiftRem)-shiftRem.index((shiftRem[-1] % number)*10)    

def solve(limit):
    longest = 0     #Used to store the final result (Denominator which leads to longest reciprocating cycle) 
    cycleLen = 0    #Current cycle length 
    #Looping through all possible denominators 
    for denom in range(2,limit):
        if countCycleLen(denom,False) >= cycleLen:
            cycleLen = countCycleLen(denom,False)
        if cycleLen >= longest:
            longest = denom
    return longest

for i in range(2,11):
    print("Remainder: ", end='')
    countCycleLen(i,True)
print("Solution Found: ",solve(limit))
