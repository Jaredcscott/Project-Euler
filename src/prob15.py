#grid = [['a','b','c'],['d','e','f'],['g','h','i']]
#start = grid[0][0]
#for y in range(len(grid)):
#    for x in range(len(grid[0])):
#        print(grid[y][x])
#for i in grid:
#    print(i)
#print(start)
#gridSize = 20 
#numOfPaths = 1
#for i in range(gridSize):
#    numOfPaths *= (2 * gridSize) - i
#    numOfPaths /= i + 1
#    
#print(numOfPaths)
masterNums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
curRow = []
row = 0
gridSize = 5
grid = []
for i in range(gridSize):
    #grid.append([])
    if i == 0:
        curRow.append(0)
        for j in range(gridSize - 1):
            curRow.append(j)
    else:    
        curRow.append(masterNums[row + i:(row + i) + 6])
    print(curRow)
    grid.append(curRow)
    curRow.clear()

for row in grid:
    print(row)