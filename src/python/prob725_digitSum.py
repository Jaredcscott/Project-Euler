'''
  @Author Jared Scott ☯
  solves the problem through comination iteration, takes a LOOOOOOOOOOOOOOOONG time
'''

def digitSum(limit):
  nums = []
  num = 1
  while len(str(num)) <= limit:
    num += 1
    for char in str(num):
      numA = int(char)
      remChar = str(num).replace(char,'',1)
      curSum = 0
      for let in remChar:
        curSum += int(let)
      if (numA == curSum):
        nums.append(num)
        break
  return sum(nums)

# Checking that the algorithm is functioning properly with known outputs
print(digitSum(3))
print(digitSum(7))
print(digitSum(2020))
