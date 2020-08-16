masterNums = [x for x in range(1,500)]
curRow = []
gridSize = 21
grid = []
for i in range(gridSize):
    if i == 0:
        curRow.append(0)
        for j in range(1,gridSize):
            curRow.append(j)
        grid.append(curRow.copy())
        curRow.clear()
    else:    
        grid.append(masterNums[i - 1:(i - 1) + gridSize])

startx = 0
starty = 0


for row in grid:
    for num in row:
        numString = "{:2}".format(num)
        row[row.index(num)] = numString
    
    print(row)
  

    

    