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


