import random, re

def getRandomLine(rsv):
    file_h = open(rsv)                  #a file handle for the .txt in question
    limit = file_h.readline()           #the number of lines to search per the .txt
    limit = limit.replace('\n', '' )    #trim the return character
    limit = int(limit)                  #the number literal converted to int
    line = random.randint(0, limit - 1) #which line to search
    
    for x in range(line):
        file_h.readline()               #parse through that shit until search reached
    phrase = file_h.readline()          #if you gotta big d*** lemme search it. 
    phrase = phrase.replace('\n', '')   #get rid of trailing returns cause those are gross
    
    return(phrase)

def magicCheck(Class, Alignment):
    if 'Good' in Alignment:
        return 'Sorcerer'
    elif 'Evil' in Alignment:
        return 'Warlock'
    else:
        return 'Wizard'

def getChar():
    Alignment = getRandomLine('alignment.txt')
    Race = getRandomLine('race.txt')        #get a random pattern
    Class = getRandomLine('class.txt')
    if Class == 'MagicUser':
        Class = magicCheck(Class, Alignment)
    if Class == 'Paladin':
        Alignment = 'Lawful Good'
    Char = Alignment + "\n" + Race + "\n" + Class
    return(Char)
    
print(getChar())