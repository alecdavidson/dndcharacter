##Alec Davidson - Summer 2014

import random, re

def getRandomLine(rsv):                 # GetRandomLine code created by David. Those comments were his.
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

def classCount():                       # This returns the number classes available
    file_h = open('class.txt')
    count = file_h.readline()
    
    return int(count)

def bardbarianCheck(Alignment):         # Bards and Barbarians cannot be lawful, rechoose if they get a lawful alignment
    if 'Lawful' in Alignment:
        Alignment = getRandomLine('alignment.txt')
        Alignment = bardbarianCheck(Alignment)
    return Alignment

def druidCheck(Alignment):              # Druids must have a neutral alignment, rechoose if they do not get a neutral alignment
    if 'Neutral' not in Alignment:
        Alignment = getRandomLine('alignment.txt')
        Alignement = druidCheck(Alignment)
    return Alignment

def monkCheck(Alignment):               # Monks must have a lawful alignment, rechoose if they do not get a lawful alignment
    if 'Lawful' not in Alignment:
        Alignment = getRandomLine('alignment.txt')
        Alignment = monkCheck(Alignment)
    return Alignment

def checkAlign(Class,Alignment):        # Run to check the alignment. If a conflict is found the alignment is repicked. Paladins are always lawful good.
    if Class == 'Bard':
        Alignment = bardbarianCheck(Alignment)
    elif Class == 'Barbarian':
        Alignment = bardbarianCheck(Alignment)
    elif Class == 'Paladin':
        Alignment = 'Lawful Good'
    elif Class == 'Druid':
        Alignment = druidCheck(Alignment)
    elif Class == 'Monk':
        Alignment = monkCheck(Alignment)
    
    return(Alignment)

def getRace():                          # Randomly pick a race from the list
    Race = getRandomLine('race.txt')
    return Race

def getClass():                         # Randomly pick a class from the list
    Class = getRandomLine('class.txt')
    return Class

def getAlign(Class):                    # Randomly pick an alignment from the list
    Alignment = getRandomLine('alignment.txt')
    Alignment = checkAlign(Class, Alignment)
    return Alignment

def getTrait():                         # Randomly pick a trait from the list
    trait = getRandomLine('traits.txt')
    
    return trait
