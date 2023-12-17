import re
f = open('inputs.txt', 'r')
sum = 0

for item in f:
    item = re.findall('[0-9]', item)
    print(item)
    
    firstItem = str(item[0])
    
    length = len(item) - 1
    maxItem = str(item[length])
    
    newItem = firstItem + maxItem
    print(newItem)
    
    sum = sum + int(newItem)
    
print(sum)