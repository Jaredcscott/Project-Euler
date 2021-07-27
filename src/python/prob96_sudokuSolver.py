import time
def main():
    #----------------------CONSTANTS------------------------------------
    SOLUTIONS_FILEPATH = "C:\\Users\\jscott\\Desktop\\Code-Library\\Python\\Specific_Problems\\Sudoku_Solver\\solutions.dat"
    PUZZLES_FILEPATH = "C:\\Users\\jscott\\Desktop\\Code-Library\\Python\\Specific_Problems\\Sudoku_Solver\\puzzles.txt"
    start_time = time.time()
    #----------------------Loading previous solutions--------------------
    solutions = loadSols(SOLUTIONS_FILEPATH)
    print(len(solutions)," Solutions Loaded")
    if len(solutions) == 0:
        for i in range(1,51):
            solutions[i] = False
    #----------------------Start of solution-----------------------------        
    puzzles = readPuzzles(PUZZLES_FILEPATH)
    for puzzle in puzzles:
        puzStr = puzzle.name.split(" ")[1].strip(' "\'\t\r\n')
        puzNum = int(puzStr)
        if str(solutions[puzNum]).strip(' "\'\t\r\n') == "False": 
            print("\nAttempting: " + puzzle.name)
            puzzle.solveRecursive()
            solutions[puzNum] = puzzle.digits 
    #----------------------Reporting results-----------------------------
    solved = 0
    for puzzle in solutions:
        result = solutions[puzzle]
        if str(result).strip() != "False":
            solved += 1 
    print("\n" + str(solved) + "/50 Puzzles Solved!")
    seconds = time.time() - start_time
    minutes = 0 
    while seconds > 60:
        minutes += 1
        seconds -= 60
    print("Runtime: " + str(minutes) + ":" + (str(int(seconds)) if seconds>9 else "0"+ str(int(seconds))))
    #----------------------Storing solutions-----------------------------
    file = open(SOLUTIONS_FILEPATH,"wt")
    sum = 0
    for solution in solutions:
        sum += int(solutions[solution])
        file.write(str(solution) + ":" + str(solutions[solution]).strip(' "\'\t\r\n') + "\n")
    print("Sum: " + str(sum))
    file.close()

    
class Puzzle:
    def __init__(self,name,rows):
        self.name = name.strip()
        self.rows = rows 
        self.cols = self.__extractCols()
        self.sqrs = self.__extractSqrs()
        self.digits = ""
                
    def potentialValues(self,row,col):
        #Assume all potentials
        potentialValues = ['1','2','3','4','5','6','7','8','9']
        #Ignore if value already present
        if str(self.rows[row][col]) != "0":
            return [self.rows[row][col]]
        #Determining which 'square' the value exists within
        sqrIndex = self.getSqr(row,col)
        #Populating values from associated groups 
        checkRow = self.rows[row] 
        checkCol = self.cols[col]
        checkSqr = self.sqrs[sqrIndex]  
        #Removing all chars which already present
        for char in str(checkRow):
            if char in potentialValues:
                potentialValues.remove(char) 
        for char in str(checkCol):
            if char in potentialValues:
                potentialValues.remove(char) 
        for char in str(checkSqr):
            if char in potentialValues:
                potentialValues.remove(char)  
        #Only potential values remain in list
        return potentialValues
        
    def updateVal(self,row,col,val):
        #Strings are immutable, creating list representation of row string
        tempList = list(self.rows[row])
        tempList[col] = val #Assigning value
        #Replacing row String 
        self.rows[row] = ''.join(tempList)
        #Adjusting columns and square representations
        self.cols = self.__extractCols() 
        self.sqrs = self.__extractSqrs()  

    def getEmptyCells(self):
        cells = []
        #Looping through grid, adding empty cell locations to the list of cells
        for row in range(9):
            for col in range(9):
                curRow = self.rows[row]
                if curRow[col] == '0':
                    cellLoc = (row,col)
                    cells.append(cellLoc)
        return cells
        
    def solveRecursive(self):
        #Checking if puzzle is solved 
        if self.isSolved():
            print("-----------------------------------------------------SOLUTION FOUND")
            self.prettyPrint()
            self.digits = self.rows[0][:3] #Storing numbers for final sum
            return True
        else:
            #Generating a queue of empty cells 
            queue = self.getEmptyCells()
            #Pulling first item in queue
            curRow = queue[0][0]
            curCol = queue[0][1] 
            #Looping through potential values at that cell location
            for val in self.potentialValues(curRow,curCol):
                #Trying value
                self.updateVal(curRow,curCol,val)
                if not self.solveRecursive():
                    #Resetting value if solution not found 
                    self.updateVal(curRow,curCol,'0') 
            return False   
    
    def getSqr(self,row,col):
        #Using range flags to determining which square the given location resides within
        if row >= 0 and row < 3:
            if col >= 0 and col < 3: 
                sqrIndex = 0
            elif col >= 3 and col < 6:
                sqrIndex = 1
            elif col >= 6 and col < 9:
                sqrIndex = 2
        elif row >= 3 and row < 6:
            if col >= 0 and col < 3: 
                sqrIndex = 3
            elif col >= 3 and col < 6:
                sqrIndex = 4
            elif col >= 6 and col < 9:
                sqrIndex = 5
        elif row >= 6 and row < 9:
            if col >= 0 and col < 3: 
                sqrIndex = 6
            elif col >= 3 and col < 6:
                sqrIndex = 7
            elif col >= 6 and col < 9:
                sqrIndex = 8
        return sqrIndex
    
    def solvePuzzle(self,times):
        #Attempt at solving the puzzle through pure logic
        time = 0
        emptySpaces = 81
        while time < times:
            for row in range(9):
                for col in range(9):
                    potVals = self.potentialValues(row,col)
                    if len(potVals) == 1:
                        self.updateVal(row,col,potVals[0])
            if self.countEmpty() == 0:
                print("Puzzle Solved!")
                self.digits = self.rows[0][:3]
                return
            left = self.countEmpty()
            if left < emptySpaces:
                emptySpaces = left 
                print("Empty Spaces: ",left)
            time += 1         

    def getCellVal(self,row,col):
        return self.rows[row][col]
                          
    def countEmpty(self):
        emptyCount = 0
        for row in self.rows:
            line = str(row)
            for char in line:
                if char == '0':
                    emptyCount += 1
        return emptyCount
        
    def isSolved(self):
        if self.countEmpty() == 0:
            return True 
        else:
            return False 
            
    def __extractCols(self):
        cols = []
        for col in range(len(self.rows)):
            curCol = []
            for row in self.rows:
                curCol.append(row[col])            
            cols.append(''.join(curCol))
        return cols 
        
    def __extractSqrs(self):
        #Poorly written range flag square extraction
        sqrs = []
        left, center, right = [], [], []
        for row in range (0,3):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col]) 
        sqrs.append(''.join(left))
        sqrs.append(''.join(center))
        sqrs.append(''.join(right))
        left, center, right = [], [], []
        for row in range(3,6):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col])
        sqrs.append(''.join(left))
        sqrs.append(''.join(center))
        sqrs.append(''.join(right))
        left, center, right = [], [], []
        for row in range(6,9):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col])
        sqrs.append(''.join(left))
        sqrs.append(''.join(center))
        sqrs.append(''.join(right))
        return sqrs
        
    def prettyPrint(self):
        print(self.name,"\nRemaining Empty Spaces: ",self.countEmpty())
        countRow = 0
        for row in self.rows:
            countCol = 0
            for val in row:
                print(val,end='')
                countCol += 1
                if countCol % 3 == 0 and countCol != 9:
                    print('|',end='')
            countRow += 1        
            if countRow  % 3 == 0 and countRow  != 9:
                print('\n-----------')
            else:
                print()
            
    def __str__(self):
        return "Name: " + self.name + "\nRows: " + str(self.rows) + "\nCols: " + str(self.cols) + "\nSqrs: " + str(self.sqrs) + "\n\n"

def loadSols(filepath):
    solutions = {}
    file = open(filepath,"r")
    data = file.readlines()
    if len(data) > 1:
        for solution in data:
            curSol = solution.split(":")
            solutions[int(curSol[0])] = curSol[1]
    file.close()
    return solutions   

def readPuzzles(filepath):    
    file = open(filepath,'r')
    lines = file.readlines()
    puzzles = []
    curPuzzle = []
    for line in lines:
        if line[0:4] == "Grid":
            name = line
        else:
            curPuzzle.append(line.strip())
        if len(curPuzzle) == 9:
            puzzles.append(Puzzle(name,curPuzzle))
            curPuzzle = []
    file.close()
    return puzzles 
      
main()
