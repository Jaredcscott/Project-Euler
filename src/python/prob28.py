x = 1001
y = 1001
curNum = x * y
grid = []
for i in range(y):
    list = []
    for j in range(x):
        list.append([])
    grid.append(list)
grid[y//2][x//2] = 1
done = x //2
count = 0
#
#for j in range(1,x+1):
#    grid[count][-j] = curNum
#    curNum -= 1
#for i in range(1,y):
#    grid[i][count] = curNum
#    curNum -= 1
#for i in range(1,x):
#    grid[y-1][i] = curNum
#    curNum -= 1
#for i in range(2,y):
#    grid[-i][-1] = curNum
#    curNum -= 1
#    pass


#for j in range(1+1,x):
#    grid[count +1][-j] = curNum
#    curNum -= 1
#for i in range(1+1,y-1):
#    grid[i][count +1] = curNum
#    curNum -= 1
#for i in range(1+1,x-1):
#    grid[y-2][i] = curNum
#    curNum -= 1
#for i in range(3,y-1):
#    grid[-i][-2] = curNum
#    curNum -= 1
#    pass

#for j in range(1+2,x-1):
#    grid[count +2][-j] = curNum
#    curNum -= 1
#for i in range(1+2,y-2):
#    grid[i][count +2] = curNum
#    curNum -= 1
#for i in range(1+2,x-2):
#    grid[y-3][i] = curNum
#    curNum -= 1
#for i in range(4,y-2):
#    grid[-i][-3] = curNum
#    curNum -= 1
#    pass
while count <= done:
    for j in range(1+count,(x+1)-count):
        grid[count][-j] = curNum
        curNum -= 1
    for i in range(1+count,y-count):
        grid[i][count] = curNum
        curNum -= 1
    for i in range(1+count,x-count):
        grid[y-(count+1)][i] = curNum
        curNum -= 1
    for i in range(2+count,y-count):
        grid[-i][-1 -(count)] = curNum
        curNum -= 1
    
    count += 1

sum = 0
for i in grid:
    print(i)
for i in range(1):
    for j in range(y):
        #print(grid[j][j])
        sum += grid[j][j]
for i in range(1):
    for j in range(1,y+1):
        #print(grid[j-1][-j])
        sum += grid[j-1][-j]
print(sum-1)
        
#print(size)