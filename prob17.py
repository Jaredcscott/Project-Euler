nums = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen', 'sixteen','seventeen','eighteen','nineteen','twenty','thirty','fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
wordsList = []
for i in range(1,31):
    if i <= 20:
        wordsList.append(nums[i])
    if i > 20 and i < 30:
        wordsList.append(nums[20])
        wordsList.append(nums[i%20])


print(wordsList)

    
