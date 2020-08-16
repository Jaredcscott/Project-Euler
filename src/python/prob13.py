from longNumber import longNum

sum = 0
for line in file:
    sum += int(line.strip())
    
print(sum)
print(str(sum)[:11])