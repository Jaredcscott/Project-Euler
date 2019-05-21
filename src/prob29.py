nums = []
for i in range(2,101):
    for j in range(2,101):
        if i ** j not in nums:
            nums.append(i ** j)
print(len(nums))
        