import regex as re
f = open('inputs.txt', 'r')
sum = 0

digitDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

for item in f:
    allDigits = []
    posDigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    
    item = re.findall('one|two|three|four|five|six|seven|eight|nine|[0-9]', item, overlapped=True)
    
    print(item)
    
    for i in item:
        if i.isdigit():
            allDigits.append(i)
        else:
            allDigits.append(digitDict[i])
    
    print(allDigits)
    
    firstItem = str(allDigits[0])
    
    length = len(allDigits) - 1
    maxItem = str(allDigits[length])
    
    newItem = firstItem + maxItem
    print(newItem)
    
    sum = sum + int(newItem)
    
print(sum)