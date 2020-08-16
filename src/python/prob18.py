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