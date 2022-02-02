'''
    @Author Jared Scott ☯
    This relies on a file of all possible pandigital numbers having already been generated. 
    To generate such a file, see ./Number_Generators/generatePandigitalNums.py
    Chews through a file containing all pandigital numbers summing those which adhere to a divisibility condition 
'''

def check_divisibility(num):
    divisors = [2,3,5,7,11,13,17] #From the problem definition for Project Euler problem # 43
    numStr = str(num) 
    check = [] #A list to contain the sub-strings from the pandigital number being checked 
    for digit in range(1,len(numStr)-3):
        #Extracting substrings 
        check.append(int(numStr[digit] + numStr[digit+1] + numStr[digit+2]))
    allTrue = False 
    index = 0
    for substring in check:
        #Checking if substrings adhere to divisibility condition 
        if (substring % divisors[index] == 0):
            allTrue = True 
        else:
            return(False)
        index += 1
    if allTrue:
        #All substrings of the current pandigital have been checked 
        print("Found one!: " + numStr,end='') 
    return(allTrue)
    
def main():
    #Opening the data file and reading in the pandigital numbers 
    number_file = open(".\\Number_Sets\\pandigital_nums.dat","r") 
    nums = number_file.readlines()
    sumVals = [] #A list to store all the numbers meeting the divisibility condition 
    for num in nums:
        #Extracting the pandigital numbers from whole set 
        if check_divisibility(num):
            sumVals.append(num) 
    sum = 0 
    for val in sumVals:
        #Summing the relevant values 
        sum += int(val) 
        
    print("Sum of pandigital numbers with divisibility property: " + str(sum)) 
    
if __name__ == '__main__':
    main()
