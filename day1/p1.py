#import regex and the inputs
import re
f = open('inputs.txt', 'r')

#set sum to 0
sum = 0

#split inputs by each item
for item in f:
    
    #find 0 to 9 in the item and print the item for debug
    item = re.findall('[0-9]', item)
    print(item)
    
    #set the first item to be the first occuring number
    firstItem = str(item[0])
    
    #set the length and then find the max item, which is at the end
    length = len(item) - 1
    maxItem = str(item[length])
    
    #create the final number by adding the first item to the last item; then, print them for debug
    newItem = firstItem + maxItem
    print(newItem)
    
    #add the new item (set to an integer) to the sum
    sum = sum + int(newItem)
    
#print out the sum
print(sum)