#####SOLUTION#####
#gridSize = 20 
#numOfPaths = 1
#for i in range(gridSize):
#    numOfPaths *= (2 * gridSize) - i
#    numOfPaths /= i + 1
#    
#print(numOfPaths)
##################


masterNums = [x for x in range(1,500)]
curRow = []
gridSize = 25
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
    
####FOR EASE OF READING####
for row in grid:
    for num in row:
        numString = "{:2}".format(num)
        row[row.index(num)] = numString
    
    print(row)
###########################    

    
####PRODUCT OF MAIN DIAGONAL?########    
#product = 1
#for i in range(gridSize):
#    print(product)
#    product *= int(grid[i][i])
#    print(product)
#
#print("Final: " + str(product))
#####################################
    
    