nums = []
for numer in range(10,100):
  for denom in range(10,100):
    if(denom > numer):
      for letter in str(numer):
        if (letter in str(denom)):
          numerS = str(numer).replace(letter,'',1)
          denomS = str(denom).replace(letter,'',1)
          if(denomS == str(0) or numer % 10 == 0):
            continue
          if(numer/denom == int(numerS)/int(denomS)):
            nums.append(str(numer) + "/" + str(denom))


product = 1
for num in nums:
  product = product * eval(num)
print(nums)