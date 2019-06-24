#grid = [['a','b','c'],['d','e','f'],['g','h','i']]
#start = grid[0][0]
#for y in range(len(grid)):
#    for x in range(len(grid[0])):
#        print(grid[y][x])


#for i in grid:
#    print(i)

#print(start)

gridSize = 20 
numOfPaths = 1
 
for i in range(gridSize):
    numOfPaths *= (2 * gridSize) - i
    numOfPaths /= i + 1
    
print(numOfPaths)
