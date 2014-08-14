##Alec Davidson - Summer 2014

import statNumb, dndcharacter

stats = []                              # The final stats are created blank and will be appended to later
charStats = [0,0,0,0,0,0]               # The character stats are set to all 0's by default
classList = []                          # Class list is used to keep track of all used classes so there are no repeats unless more characters are requested than there are classes
classCount = dndcharacter.classCount()  # Obtain the number of classes that are available

race = ""
race2 = ""
clas = ""
align = ""
trait1 = ""
trait2 = ""

def is_number(s):                       # This function will be used to make sure that a number is entered for the party size, any other option defaults to 1
    try:
        int(s)
        return True
    except ValueError:
        return False

def classCheck():                       # This function is used to make sure the randomly chosen class has not alredy been used, if it has a new one will be chosen
    global classList, clas
    if clas in classList:
        clas = dndcharacter.getClass()
        classCheck()

def reset():                            # All traits are saved and the same character is printed out X times, a reset function fixes this by ensuring everything is re-randomly selected
    global stats, charStats, race, clas, align, race2, trait1, trait2
    
    stats = []
    charStats = [0,0,0,0,0,0]
    race = dndcharacter.getRace()       # Use the dndcharacter file to obtain the different elements of a character
    clas = dndcharacter.getClass()
    classCheck()
    align = dndcharacter.getAlign(clas)
    race2 = race                        # For ease, hyphenated races will remove the hyphen, so a second race variable is included that is untouched until it is printed
    trait1 = dndcharacter.getTrait()
    trait2 = dndcharacter.getTrait()

def traitCheck():                       # To ensure the same two traits are not selected, this function changes the second trait until it is not the first one 
    global trait1, trait2
    
    if trait2 == trait1:
        trait2 = dndcharacter.getTrait()
        traitCheck()
## Note to self, get rid of all these
##   if statements and make it look nicer
##   more text files? py files? functions?
if race == "Half-Elf":                  # This changes hyphenated races to unhyphenated for ease of use
    race2 = "Half-Elf"
    race = "HalfElf"
elif race == "Half-Orc":                # Hal-Elf and Half-Orc are the only races that fit this description
    race2 = "Half-Orc"
    race = "HalfOrc"

def raceStat(race):                     # This will change the character stat to reflect race bonuses
    global charStats
    if race == "Human":                 # Each race has a different plus or minus bonus on stats, each are set here
        charStats = [0,0,0,0,0,0]       # The stats are [strength, dexterity, constitution, intelligence, wisdom, charisma] in that order
    elif race == "Dwarf":
        charStats = [0,0,2,0,0,-2]
    elif race == "Elf":
        charStats = [0,2,-2,0,0,0]
    elif race == "Gnome":
        charStats = [-2,0,2,0,0,0]
    elif race == "HalfElf":
        charStats = [0,0,0,0,0,0]
    elif race == "HalfOrc":
        charStats = [2,0,0,-2,0,-2]
    elif race == "Halfling":
        charStats = [-2,2,0,0,0,0]
    elif race == "Turtle":               # Shout out to David for help with heroku and the getRandomLine
        charStats = [2,2,2,2,2,2]
    elif race == "Skeleton":             # And to Michael just because
        charStats = [2,2,2,2,2,5]

def main(reroll,save):                  # This is the main function, the one that actually gets called by the user
    reset()                             # First reset the variables to ensure everything is fresh
    global race
    for i in range(6):                  # Generate the six stats (the reroll determines whether or not stats below 10 should be rerolled)
        stats.append(statNumb.statRand(reroll))
    
    classCheck()                        # Run the class and trait checks and then the print Character function
    
    traitCheck()
    
    raceStat(race)
    
    printChar(save)

def clasAdd(stat,clas):                 # Take the stats and put them in the order that would best benifit the chosen class
    stat.sort()                         # Sort the stats from smallest to largest
    statFin = []                        # Create a final stat the will be returned at the end
    
    if clas == "Barbarian":             # For each class append to the final stat in order of strength to charisma
        statFin.append(stat[5]) #Str    # Each class appends in a different order depending on what is needed to play according to D&D 3.5
        statFin.append(stat[4]) #Dex
        statFin.append(stat[2]) #Con
        statFin.append(stat[0]) #Int
        statFin.append(stat[3]) #Wis
        statFin.append(stat[1]) #Cha
    ## should probably find a better way to do this
    if clas == "Bard":
        statFin.append(stat[0]) #Str
        statFin.append(stat[4]) #Dex
        statFin.append(stat[1]) #Con
        statFin.append(stat[3]) #Int
        statFin.append(stat[2]) #Wis
        statFin.append(stat[5]) #Cha
    
    if clas == "Cleric":
        statFin.append(stat[1]) #Str
        statFin.append(stat[0]) #Dex
        statFin.append(stat[4]) #Con
        statFin.append(stat[2]) #Int
        statFin.append(stat[5]) #Wis
        statFin.append(stat[3]) #Cha

    if clas == "Druid":
        statFin.append(stat[0]) #Str
        statFin.append(stat[4]) #Dex
        statFin.append(stat[2]) #Con
        statFin.append(stat[3]) #Int
        statFin.append(stat[5]) #Wis
        statFin.append(stat[1]) #Cha
    
    if clas == "Fighter":
        statFin.append(stat[5]) #Str
        statFin.append(stat[3]) #Dex
        statFin.append(stat[4]) #Con
        statFin.append(stat[0]) #Int
        statFin.append(stat[2]) #Wis
        statFin.append(stat[1]) #Cha
    
    if clas == "Monk":
        statFin.append(stat[3]) #Str
        statFin.append(stat[4]) #Dex
        statFin.append(stat[2]) #Con
        statFin.append(stat[1]) #Int
        statFin.append(stat[5]) #Wis
        statFin.append(stat[0]) #Cha
    
    if clas == "Paladin":
        statFin.append(stat[4]) #Str
        statFin.append(stat[2]) #Dex
        statFin.append(stat[4]) #Con
        statFin.append(stat[0]) #Int
        statFin.append(stat[3]) #Wis
        statFin.append(stat[5]) #Cha
    
    if clas == "Ranger":
        statFin.append(stat[4]) #Str
        statFin.append(stat[5]) #Dex
        statFin.append(stat[1]) #Con
        statFin.append(stat[2]) #Int
        statFin.append(stat[3]) #Wis
        statFin.append(stat[0]) #Cha
    
    if clas == "Rogue":
        statFin.append(stat[1]) #Str
        statFin.append(stat[4]) #Dex
        statFin.append(stat[0]) #Con
        statFin.append(stat[3]) #Int
        statFin.append(stat[2]) #Wis
        statFin.append(stat[5]) #Cha
    
    if clas == "Sorcerer":
        statFin.append(stat[0]) #Str
        statFin.append(stat[4]) #Dex
        statFin.append(stat[3]) #Con
        statFin.append(stat[2]) #Int
        statFin.append(stat[1]) #Wis
        statFin.append(stat[5]) #Cha
    
    if clas == "Wizard":
        statFin.append(stat[0]) #Str
        statFin.append(stat[4]) #Dex
        statFin.append(stat[3]) #Con
        statFin.append(stat[5]) #Int
        statFin.append(stat[1]) #Wis
        statFin.append(stat[2]) #Cha
    
    return statFin
    
def statAdd(stat1,stat2):               # This adds the race stats to the class stats
    global race
    statFin = []
    for i in range(6):
        statFin.append(stat1[i] + stat2[i])
    if race == "HalfOrc":
        if statFin[3] < 3:
            statFin[3] = 3
    return statFin

def textAdd(stat):                      # Adds text for readability
    statFin = []
    statFin.append("Str: "+str(stat[0]))
    statFin.append("Dex: "+str(stat[1]))
    statFin.append("Con: "+str(stat[2]))
    statFin.append("Int: "+str(stat[3]))
    statFin.append("Wis: "+str(stat[4]))
    statFin.append("Cha: "+str(stat[5]))
    
    return statFin

def printChar(save):                    # The pretty part, this prints everything out and adds the class to the class list to ensure no duplicates
    global classList
    
    if save:
        chartxt = open("chartxt.txt", "a")
        chartxt.write("-------------------------\n")
        chartxt.write("Alignment: " + align + "\n")
        chartxt.write("Race: " + race2 + "\n")
        chartxt.write("Class: " + clas + "\n")
        chartxt.write("Traits: " + trait1 + ", " + trait2 + "\n")
        chartxt.write("Stats: " + str(textAdd(statAdd(charStats,clasAdd(stats,clas)))) + "\n") # Takes the random stats and changes the order to fit the class, adds the race bonuses, and adds text for readability.

    else:
        print("")    
        print("Alignment: " + align)
        print("Race: " + race2)
        print("Class: " + clas)
        print("Traits: " + trait1 + ", " + trait2)
        print("Stats: " + str(textAdd(statAdd(charStats,clasAdd(stats,clas))))) # Takes the random stats and changes the order to fit the class, adds the race bonuses, and adds text for readability.
        
    classList.append(clas)



                                        # This asks for the size of the party
party = raw_input("Generate how many characters? (There are "+str(classCount)+" different class options)\n")
                                        # This askes for if the user wants to reroll stats under 10 or not
reroll = raw_input("Re-Roll Stats under 10? (leave blank if no)\n")
                                        # The party size is then used to generate however many characters
                                        # Neat feature, will remove for webapp probably
save = raw_input("Save to text file? (Leave blank for no)\n")
if is_number(party):
    for i in range(int(party)):
        if i%classCount == 0:
            classList = []
        main(reroll,save)
else:
    main(reroll,save)
