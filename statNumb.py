##Alec Davidson - Summer 2014

import random, re

def statRand(reroll):                   # This is used to generate random stats the same why they would be created with dice
    
    total = 0
    totalList = []
    
    for i in range(1,5):                # Four six sided dice
        totalList.append(random.randrange(1,7))
    
    totalList.sort()
    totalList.reverse()
    totalList.pop()                     # Remove the smallest
    
    for i in range(0,3):
        total += totalList[i]
    
    if reroll.lower() != "no":# If wanted all totals under 10 will be rerolled
        if total < 10:
            return statRand(reroll)
    
    return total