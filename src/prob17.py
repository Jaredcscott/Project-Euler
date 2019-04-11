nums = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen', 'sixteen','seventeen','eighteen','nineteen','twenty','thirty','fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
wordsList = []
for i in range(1,1001):
    if i % 100 == 0 and i != 1000:
        wordsList.append(nums[int(str(i)[0])])
        wordsList.append('hundred')
    if i <= 20:
        wordsList.append(nums[i])
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
        wordsList.append(nums[23])
    if int(str(i)[-2:]) > 60 and int(str(i)[-2:]) < 70:
        #print(int(str(i)[-2:]))
        wordsList.append(nums[23])
        wordsList.append(nums[int(str(i)[-2:])%70])


print(wordsList)

    
