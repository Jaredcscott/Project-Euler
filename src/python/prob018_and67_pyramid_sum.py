'''
    @Author Jared Scott ☯
    This file contains the logic for solving both problems 18 and 67 of Project Euler
    Using a dynamic programming approach I recursively scan the paths comparing their outputs stepwise
'''
def find_max_path(curRow,curCol,cache,pyramid):
    #First check to see if the answer has already been found
    sol = cache.get((curRow,curCol))
    if sol:
        return sol
    #Current path is not the largest sum, restarting the sum for a new path calculation
    if curRow >= len(pyramid):
        cur_sum = (0,[],[])
    else:
        #Main solution logic...
        curVal = pyramid[curRow][curCol]
        #Check the two possible moves recursively to find the shortest path
        sum_1, row_1, col_1 = find_max_path(curRow + 1, curCol, cache, pyramid) 
        sum_2, row_2, col_2 = find_max_path(curRow + 1, curCol + 1, cache, pyramid) 
        #Comparing the results of the two paths to determine which one is larger 
        if sum_1 > sum_2:
            cur_sum = (curVal+sum_1, [curVal]+row_1, [curCol]+col_1) 
        else: 
            cur_sum = (curVal+sum_2, [curVal]+row_2, [curCol]+col_2) 
    #Store max sum at current location into the cache until the top is reached        
    cache[(curRow,curCol)] = cur_sum
    return cur_sum
      
def read_file(filePath):
    #Utility function to read pyramid form file and convert into a iterable list
    with open(filePath) as f:
        input_list = f.readlines()
        output_list = []
        for line in input_list:
            cur_line = []
            nums = line.split(" ")
            for num in nums:
                cur_line.append(int(num))
            output_list.append(cur_line)
    return output_list
    
    
    
def main():
    #Solving for small pyramid
    cache = {}
    pyramid_small = [
      [75],
      [95, 64],
      [17, 47, 82],
      [18, 35, 87, 10],
      [20, 4, 82, 47, 65],
      [19, 1, 23, 75, 3, 34],
      [88, 2, 77, 73, 7, 63, 67],
      [99, 65, 4, 28, 6, 16, 70, 92],
      [41, 41, 26, 56, 83, 40, 80, 70, 33],
      [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
      [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
      [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
      [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
      [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
      [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
    small_sol = find_max_path(0,0,cache,pyramid_small)
    print("Path Found!\nSum: " + str(small_sol[0]) + "\nPath: " + str(small_sol[1]))
    #Solving for big pyramid
    pyramid_big = read_file('p067_triangle.txt')
    cache = {}
    big_sol = find_max_path(0,0,cache,pyramid_big)
    print("\nPath Found!\nSum: " + str(big_sol[0]) + "\nPath: " + str(big_sol[1]))
    
if __name__ == "__main__":
    main()
