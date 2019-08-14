nums = []
for i in range(2,10999999):
    numSum = 0
    numString = str(i)
    for j in numString:
        numSum += int(j)**5
        if numSum > i:
            break
    if numSum == i:
        print("Number added")
        nums.append(i)
    if i % 300000 == 0:
        print(i)
print(nums)
print(sum(nums))
        