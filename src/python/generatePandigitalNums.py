'''
    @Author Jared Scott ☯
    This will take a few hours to finish complete generation.
    Values will be output to the indicated file as they are generated making them available before complete 
    Iteratively generates all possible pandigital numbers.
'''
def isPanDigital(num):
    nums = []
    duplicateNums = False
    numStr = str(num)
    numLen = len(numStr)
    for char in numStr:
        if char in nums:
            return(False)
        else:
            nums.append(char) 
          
    nums.sort()
    #Within python integers with a leading 0 will be truncated
    if nums == ['0','1','2','3','4','5','6','7','8','9'] or nums == ['1','2','3','4','5','6','7','8','9']:
        return(True)
    return(False)    

def generate_pandigital_nums(limit,path):
    outputFile = open(path,"w")
    val = 123456789
    count = 0
    while val < limit:
        if isPanDigital(val):
            if len(str(val)) == 10:
                line = "0" + str(val) 
                outputFile.write(str(line))
                continue
            outputFile.write(str(val) + "\n")
        val += 1
        count += 1
        if count % 250000 == 0:
            print("Working...Last value tried: " + str(val))
    outputFile.close()

def main():        
    path = "pandigital_nums.dat"
    generate_pandigital_nums(9999999999,path)    
    
if __name__ == '__main__':
    main()
