##Alec Davidson - Summer 2014

import random, re, ast, pathlib

path = pathlib.Path(__file__).parent.absolute()

def getRandomLine(rsv):
    global path

    file_h = open(f"{path}\{rsv}")
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
    Race = ast.literal_eval(getRandomLine('race.txt'))
    return Race

def getClass():
    Class = ast.literal_eval(getRandomLine('class.txt'))
    return Class

def getAlign(Class):
    Alignment = getRandomLine('alignment.txt')
    #Alignment = checkAlign(Class, Alignment)
    return Alignment

def getTrait(type):
    trait = getRandomLine(type + '.txt')

    return trait
