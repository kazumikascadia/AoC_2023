#open inputs
f = open('input.txt', 'r')

#debug games
games = ['Game 1: 14 green, 8 blue, 9 red; 5 blue, 4 green, 2 red; 4 red, 4 blue, 4 green; 1 blue, 3 green, 2 red; 10 red, 3 blue, 15 green; 2 red, 6 green, 3 blue', 'Game 2: 1 red, 12 green, 2 blue; 2 green, 1 blue, 1 red; 4 green, 2 blue; 10 green, 3 blue; 4 green, 2 red, 2 blue']

#set sum and the required string
sum = 0
req = 'red: 12, green: 13, blue: 14'

#split by game
for game in f:
    
    #beautify and introduce game (for debug)
    print(' ')
    print(game)
    
    #set red, blue, and green for each game
    red = 0
    blue = 0
    green = 0
    
    gameNum = game.split(':')[0].replace('Game ', '')
    index = game.index(':')
    sections = game[index + 2:].split(';')
    
    #split by section
    for section in sections:
        
        #split into areas
        area = section.split(',')
        
        #split area by variables
        for variable in area:
            
            #find the first space
            varIndex = variable.index(' ')
            
            #if the first space is in the 0 slot, remove it; else, keep on going
            if varIndex == 0:
                variable = variable[varIndex + 1:]
            else:
                pass
            
            #print(variable)
            
            #find out if a variable has red, green, or blue; then, split the number and add it to the original sum
            if 'red' in variable:
                space = variable.index(' ')
                num = variable[:space]
                red = red + int(num)
            elif 'green' in variable:
                space = variable.index(' ')
                num = variable[:space]
                green = green + int(num)
            else:
                space = variable.index(' ')
                num = variable[:space]
                blue = blue + int(num)
    
    #debug insurance
    game = 'red: ' + str(red) + ', ' + 'green: ' + str(green) + ', ' + 'blue: ' + str(blue)
    
    #print the whole game out (for insurance)
    print(game)
    print(req)
    
    #check if it has the right amounts: if so, add them to the sum; if not, say it's not possible
    if red <= 12 and green <= 13 and blue <= 14:
        print(gameNum)
        
        sum = sum + int(gameNum)
    else:
        print('Not possible!')
  
#beautify and print the sum         
print(' ') 
print('Sum: ' + str(sum))