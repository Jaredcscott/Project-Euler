curSum = 0
curPow = 1
while curPow < 1000:
    curSum += curPow ** curPow
    curPow += 1

print(curSum)
print(str(curSum)[-10:])
