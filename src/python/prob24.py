import sys 
nums = [0,1,2,3,4,5,6,7,8,9]
nums1 = [1,2,3,4,5,6,7,8,9,0]
nums2 = [2,3,4,5,6,7,8,9,0,1]
nums3 = [3,4,5,6,7,8,9,0,1,2]
nums4 = [4,5,6,7,8,9,0,1,2,3]
nums5 = [5,6,7,8,9,0,1,2,3,4]
nums6 = [6,7,8,9,0,1,2,3,4,5]
nums7 = [7,8,9,0,1,2,3,4,5,6]
nums8 = [8,9,0,1,2,3,4,5,6,7]
nums9 = [9,0,1,2,3,4,5,6,7,8]
ordersList = []
 
for a in nums:
    for b in nums1:
        if len(ordersList) > 1500000:
            break
        if b == a:
            continue
        for c in nums2:
            if len(ordersList) > 1500000:
                break
            if c == a or c == b:
                continue
            for d in nums3:
                if len(ordersList) > 1500000:
                    break
                if d == a or d == b or d == c:
                    continue
                for e in nums4:
                    if len(ordersList) > 1500000:
                        break
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in nums5:
                        if len(ordersList) > 1500000:
                            break
                        if f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in nums6:
                            if len(ordersList) > 1500000:
                                break
                            if g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in nums7:
                                if len(ordersList) > 1500000:
                                    break
                                if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                for i in nums8:
                                    if len(ordersList) > 1500000:
                                        break
                                    if i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h:
                                        continue
                                    for j in nums9:
                                        if j == a or j == b or j == c or j == d or j == e or j == f or j == g or j == h or j == i:
                                            continue
                                        #for k in nums:
                                        #    if k == a or k == b or k == c or k == d or k == e or k == f or k == g or k == h or k == i or k == j: 
                                        #        continue
                                        #print(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))
                                        ordersList.append(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))
                                        if len(ordersList) % 1000 == 0 and len(ordersList) < 999995:
                                            print(len(ordersList))
                                        #if len(ordersList) > 999995 and len(ordersList) < 1000005:
                                            #print(len(ordersList))
                                            #print(str(len(ordersList)) + " " + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j)) 
                                        if len(ordersList) > 1500000:
                                            break
                                      

ordersList.sort()
print(ordersList[0:20])
print("999999")
print(ordersList[999997:1000005])
print("1000000")
print(ordersList[1000000])
print("1000001")
print(ordersList[1000001])