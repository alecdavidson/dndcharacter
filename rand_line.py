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