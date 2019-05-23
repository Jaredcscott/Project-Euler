nums = [0,1,2]
a = 0
b = 1
c = 2
ordersList = []
while len(ordersList) < 1:
    for a in nums:
        for b in nums:
            if b == a:
                continue
            for c in nums:
                if c == a or c == b:
                    continue
                #print(str(a) + str(b) + str(c))
                ordersList.append(str(a) + str(b) + str(c))           
    
                
  
    #if curNum not in ordersList:
    #    ordersList.append(curNum)
    #print(curNum)
#for a in range(3):
#    for b in range(3):
#        for c in range(3):
#            curNum = ''
#            if str(a) not in curNum:
#                curNum += str(a)
#            if str(b) not in curNum:
#                curNum += str(b)
#            if str(c) not in curNum:
#                curNum += str(c)  
#            print(curNum)
#            if len(curNum) == 3 and curNum not in ordersList:
#                ordersList.append(curNum)                
#                
#            
#ordersList.sort()
print(ordersList)