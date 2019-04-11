
file = open('longNum.txt', 'r')
'''
longNum = ""
for line in file:
    longNum += line.strip()

print(longNum)
'''
    
from longNumber import longNum
sum = 0
for line in file:
    sum += int(line.strip())
    
print(sum)
print(str(sum)[:11])