def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num -1)

nums = []

for i in range(1000000):
    curNum = 0
    for j in str(i):
        curNum += factorial(int(j))
    if curNum == i and i != 1 and i != 2:
        print("Found num!: " + str(i))
        nums.append(i)
    if i % 500000 == 0:
        print(i)

print(nums)
print(sum(nums))
        


