rightTriangles = []
countList = []
for i in range(1000):
    countList.append(0)
max = 0    
print(len(countList))
for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i ** 2 + j ** 2 == k ** 2 and i + j + k <= 1000:
                triangle = [i,j,k]
                triangle.sort()
                print("Found one: " + str(triangle))
                sum = i + j + k
                if triangle not in rightTriangles:
                    rightTriangles.append(triangle)
                    countList[sum - 1] += 1
                    if countList[sum - 1] > max:
                        max = countList[sum - 1]
                    print("Sum: " + str(sum) + " Count: " + str(countList[sum - 1]))                   
                
                print("Cur Max: " + str(max) + " P value: " + str(countList.index(max) + 1))
print(countList.index(max(countList)))