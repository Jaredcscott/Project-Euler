FILEPATH = "C:\\Users\\jared\\Desktop\\Code-Library\\Python\\Math\\words.txt"

LETTERS = {
    '"':0,
    '':0,
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':10,
    'K':11,
    'L':12,
    'M':13,
    'N':14,
    'O':15,
    'P':16,
    'Q':17,
    'R':18,
    'S':19,
    'T':20,
    'U':21,
    'V':22,
    'W':23,
    'X':24,
    'Y':25,
    'Z':26
}
def readData(filepath):    
    print("Reading data. . .")
    file = open(filepath,'r')
    words = []
    line = file.readline()
    words = line.split(',')
    file.close()
    return words 
   
def genTriNumbers(limit):
    triangleNums = []
    num = 1
    while num < limit:
        curNum = (num * (1 + num)) / 2 
        #if curNum > 40755:
        triangleNums.append(int(curNum))
        num += 1
    return triangleNums

def convertWord(word):
    wordSum = 0
    for letter in word:
        wordSum += LETTERS[letter]
    return wordSum
        
words = readData(FILEPATH)
triNums = genTriNumbers(2500000)
print("Printing first 10 Triangle numbers",triNums[:10])
print("Validating letters dictionary \nS=19\nK=11 \nY=25\n =55\nRESULTS:",LETTERS['S'] + LETTERS['K'] + LETTERS['Y'],"\nPASSED")
count = 0
for word in words:
    wordNum = convertWord(word)
    if wordNum in triNums:
        print("Triangle Word Found!" + word + "Number Form: " + str(wordNum))
        count += 1
print("Count of Triangle Words: " + str(count))

