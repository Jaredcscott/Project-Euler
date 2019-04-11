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