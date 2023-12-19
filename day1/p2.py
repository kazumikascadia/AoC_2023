#import regex and inputs
import regex as re
f = open('inputs.txt', 'r')

#set the sum to 0
sum = 0

#simple dictionary
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

#split f by each item
for item in f:
    #create all digits
    allDigits = []

    #find each existing number in the item, even if they overlap; then, print them    
    item = re.findall('one|two|three|four|five|six|seven|eight|nine|[0-9]', item, overlapped=True)
    print(item)
    
    #split by item and check if its a digit or not: if its a digit, add it to the array; if not, convert it using the dictionary and then append it to the array
    for i in item:
        if i.isdigit():
            allDigits.append(i)
        else:
            allDigits.append(digitDict[i])
    
    #print the array
    print(allDigits)
    
    #set the first item to be the first digit in the array
    firstItem = str(allDigits[0])
    
    #find the length and set the max item to be the last item in the array
    length = len(allDigits) - 1
    maxItem = str(allDigits[length])
    
    #add the first item to the last item (which are both strings); then, print the new item for debug
    newItem = firstItem + maxItem
    print(newItem)
    
    #add the new item to the sum
    sum = sum + int(newItem)

#print the sum for debug
print(sum)