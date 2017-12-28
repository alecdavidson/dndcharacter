##Alec Davidson - Summer 2014

import random, re

def getRandomLine(rsv):
    file_h = open(rsv)
    limit = file_h.readline()
    limit = limit.replace('\n', '' )
    limit = int(limit)
    line = random.randint(0, limit - 1)
    
    for x in range(line):
        file_h.readline()
    phrase = file_h.readline()
    phrase = phrase.replace('\n', '')
    
    return(phrase)

def classCount():
    file_h = open('class.txt')
    count = file_h.readline()
    
    return int(count)

def bardbarianCheck(Alignment):
    if 'Lawful' in Alignment:
        Alignment = getRandomLine('alignment.txt')
        Alignment = bardbarianCheck(Alignment)
    return Alignment

def druidCheck(Alignment):
    if 'Neutral' not in Alignment:
        Alignment = getRandomLine('alignment.txt')
        Alignement = druidCheck(Alignment)
    return Alignment

def monkCheck(Alignment):
    if 'Lawful' not in Alignment:
        Alignment = getRandomLine('alignment.txt')
        Alignment = monkCheck(Alignment)
    return Alignment

def checkAlign(Class,Alignment):
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

def getRace():
    Race = getRandomLine('race.txt')
    return Race

def getClass():
    Class = getRandomLine('class.txt')
    return Class

def getAlign(Class):
    Alignment = getRandomLine('alignment.txt')
    Alignment = checkAlign(Class, Alignment)
    return Alignment

def getTrait(type):
    trait = getRandomLine(type + '.txt')
    
    return trait