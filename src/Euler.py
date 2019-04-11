import random

def isPalindrome(numToCheck):
    numString = str(numToCheck)
    stringLen = len(numString)
    isEven = False 
    if stringLen % 2 == 0:
        isEven = True
    start = 0
    if not isEven:
        middle = stringLen // 2
    end = stringLen
    
    if isEven:
        i = start
        j = end - 1
        while i < stringLen and j >= 0:
            if numString[i] == numString[j]:
                i += 1 
                j -= 1
                continue
            else:
                return False
        return True
    else:
        i = start
        j = end - 1
        while i < stringLen and j >= 0:
            if i == middle:
                break
            if numString[i] == numString[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
        
listOfNum = []


for i in range(1000):
    for j in range(1000):
        if isPalindrome(i * j):
            if i * j == 0:
                continue
            listOfNum.append(i * j)
print(max(listOfNum))
