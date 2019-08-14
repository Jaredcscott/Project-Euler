nums = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen', 'sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
wordsList = []
numbers = 0
for i in range(1,1001):
    if i % 100 == 0 and i != 1000:
        wordsList.append(nums[int(str(i)[0])])
        wordsList.append('hundred')
        
    if len(str(i)) >= 3 and i != 1000 and i % 100 != 0:
        wordsList.append(nums[int(str(i)[-3])])
        wordsList.append('hundred')
        wordsList.append('and')
        
    #if i <= 20:
    #    wordsList.append(nums[i])
    if int(str(i)[-2:]) <= 20 and int(str(i)[-2:]) > 0:
        wordsList.append(nums[int(str(i)[-2:])])
        
    if int(str(i)[-2:]) > 20 and int(str(i)[-2:]) < 30:
        wordsList.append(nums[20])
        wordsList.append(nums[int(str(i)[-2:])%20])
    
    if int(str(i)[-2:]) == 30:
        wordsList.append(nums[21])
    if int(str(i)[-2:]) > 30 and int(str(i)[-2:]) < 40:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[21])
        wordsList.append(nums[int(str(i)[-2:])%30])
        
    if int(str(i)[-2:]) == 40:
        wordsList.append(nums[22])
    if int(str(i)[-2:]) > 40 and int(str(i)[-2:]) < 50:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[22])
        wordsList.append(nums[int(str(i)[-2:])%40])
        
    if int(str(i)[-2:]) == 50:
        wordsList.append(nums[23])
    if int(str(i)[-2:]) > 50 and int(str(i)[-2:]) < 60:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[23])
        wordsList.append(nums[int(str(i)[-2:])%50])
        
    if int(str(i)[-2:]) == 60:
        wordsList.append(nums[24])
    if int(str(i)[-2:]) > 60 and int(str(i)[-2:]) < 70:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[24])
        wordsList.append(nums[int(str(i)[-2:])%60])
    
    if int(str(i)[-2:]) == 70:
        wordsList.append(nums[25])
    if int(str(i)[-2:]) > 70 and int(str(i)[-2:]) < 80:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[25])
        wordsList.append(nums[int(str(i)[-2:])%70])
        
    if int(str(i)[-2:]) == 80:
        wordsList.append(nums[26])
    if int(str(i)[-2:]) > 80 and int(str(i)[-2:]) < 90:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[26])
        wordsList.append(nums[int(str(i)[-2:])%80])
        
    if int(str(i)[-2:]) == 90:
        wordsList.append(nums[27])
    if int(str(i)[-2:]) > 90 and int(str(i)[-2:]) < 100:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[27])
        wordsList.append(nums[int(str(i)[-2:])%90])
    if i == 1000:
        wordsList.append('one')
        wordsList.append('thousand')
    numbers += 1
        



print(numbers)
letters = 0
for word in wordsList:
    for letter in word:
        #print(letter)
        letters += 1
        
print(letters)


    
