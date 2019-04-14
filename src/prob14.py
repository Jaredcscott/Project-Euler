<<<<<<< HEAD
def even(num):
    return num/2
    
def odd(num):
    return (3 * num) + 1
    
num = 1 
longestChain = 0

while num < 1000000:
    chain = []
    curNum = num
    while curNum != 1:
        if curNum % 2 == 0:
            chain.append(curNum)
            curNum = even(curNum)
            chain.append(curNum)
        else:
            chain.append(curNum)
            curNum = odd(curNum)
            chain.append(curNum)
    if len(chain) > longestChain:
        print(chain)
        print("New highest!: " + str(num)
        longestChain = num

print(longestChain)
=======
largestSeq = 0
ansNum = 0
num = 1
while num < 1000000:
    curNum = num
    chain = []
    chain.append(curNum)
    while curNum != 1:
        if curNum % 2 == 0:
            curNum /= 2
            chain.append(curNum)
        else:
            curNum = (curNum * 3) + 1
            chain.append(curNum)
        #print(curNum)
    
    if len(chain) > largestSeq:
        largestSeq = len(chain)
        ansNum = num
    num += 1

print(ansNum, largestSeq)


>>>>>>> bf6bea2de390ad3ccfe4b0ebc22c268bf7413971
