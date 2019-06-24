nums = []
for i in range(1000000):
    decimalPalin = True
    binaryPalin = True 
    binaryNum = str(bin(i)[2:])
    numString = str(i)
    start = 0
    end = len(numString)
    if len(numString) % 2 == 0:
        for index in range(end // 2):
            #print(numString[index] + " " + numString[-1 - index])
            if int(numString[index]) != int(numString[-1 - index]):
                decimalPalin = False
    else:
        mid = end // 2 + 1
        for index in range(mid):
            if int(numString[index]) != int(numString[-1 - index]):
                decimalPalin = False
    
    startBin = 0
    endBin = len(binaryNum)
    if len(binaryNum) % 2 == 0:
        for index in range(endBin // 2):
            #print(binaryNum[index] + " " + binaryNum[-1 - index])
            if int(binaryNum[index]) != int(binaryNum[-1 - index]):
                binaryPalin = False
    else:        
        midBin = endBin // 2 + 1
        for index in range(midBin):
            if int(binaryNum[index]) != int(binaryNum[-1 - index]):
                binaryPalin = False
                
                
                
    if binaryPalin and decimalPalin:
        print("Num Found!!" + " " + str(i) + " " + binaryNum)
        nums.append(i)
    
    
    
    
    #print("Binary: " + binaryNum + str(binaryPalin) + " \nDecimal: " + numString + str(decimalPalin))
    
print(sum(nums))


        

