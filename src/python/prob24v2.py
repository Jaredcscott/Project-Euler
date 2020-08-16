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
    
                
  
print(ordersList)