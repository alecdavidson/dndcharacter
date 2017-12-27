##Alec Davidson - Summer 2014

import statNumb, dndcharacter, flask

stats = []
charStats = [0,0,0,0,0,0]
classList = []
classCount = dndcharacter.classCount()

race = ""
race2 = ""
race3 = "none"
clas = ""
align = ""
trait1 = ""
trait2 = ""

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def classCheck():
	global classList, clas
	if clas in classList:
		clas = dndcharacter.getClass()
		classCheck()

def reset():
	global stats, charStats, race, race2, clas, align, trait1, trait2
	
	stats = []
	charStats = [0,0,0,0,0,0]
	if race3 == "none":
		race = dndcharacter.getRace()
	else:
		race = race3
	clas = dndcharacter.getClass()
	classCheck()
	align = dndcharacter.getAlign(clas)
	race2 = race
	trait1 = dndcharacter.getTrait()
	trait2 = dndcharacter.getTrait()

def traitCheck():
	global trait1, trait2
	
	if trait2 == trait1:
		trait2 = dndcharacter.getTrait()
		traitCheck()
## Note to self, get rid of all these
##   if statements and make it look nicer
##   more text files? py files? functions?
if race == "Half-Elf":
	race2 = "Half-Elf"
	race = "HalfElf"
elif race == "Half-Orc":
	race2 = "Half-Orc"
	race = "HalfOrc"

def raceStat(race):
	global charStats
	if race == "Human":
		charStats = [0,0,0,0,0,0]
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
	elif race == "Turtle":
		charStats = [2,2,2,2,2,2]
	elif race == "Skeleton":
		charStats = [2,2,2,2,2,5]

def main(reroll):
	reset()
	global race
	for i in range(6):
		stats.append(statNumb.statRand(reroll))
	
	classCheck()
	
	traitCheck()
	
	raceStat(race)
	
	printChar()

def clasAdd(stat,clas):
	stat.sort()
	statFin = []
	
	if clas == "Barbarian":
		statFin.append(stat[5])
		statFin.append(stat[4])
		statFin.append(stat[2])
		statFin.append(stat[0])
		statFin.append(stat[3])
		statFin.append(stat[1])
	
	elif clas == "Bard":
		statFin.append(stat[0])
		statFin.append(stat[4])
		statFin.append(stat[1])
		statFin.append(stat[3])
		statFin.append(stat[2])
		statFin.append(stat[5])
	
	elif clas == "Cleric":
		statFin.append(stat[1])
		statFin.append(stat[0])
		statFin.append(stat[4])
		statFin.append(stat[2])
		statFin.append(stat[5])
		statFin.append(stat[3])

	elif clas == "Druid":
		statFin.append(stat[0])
		statFin.append(stat[4])
		statFin.append(stat[2])
		statFin.append(stat[3])
		statFin.append(stat[5])
		statFin.append(stat[1])
	
	elif clas == "Fighter":
		statFin.append(stat[5])
		statFin.append(stat[3])
		statFin.append(stat[4])
		statFin.append(stat[0])
		statFin.append(stat[2])
		statFin.append(stat[1])
	
	elif clas == "Monk":
		statFin.append(stat[3])
		statFin.append(stat[4])
		statFin.append(stat[2])
		statFin.append(stat[1])
		statFin.append(stat[5])
		statFin.append(stat[0])
	
	elif clas == "Paladin":
		statFin.append(stat[4])
		statFin.append(stat[2])
		statFin.append(stat[4])
		statFin.append(stat[0])
		statFin.append(stat[3])
		statFin.append(stat[5])
	
	elif clas == "Ranger":
		statFin.append(stat[4])
		statFin.append(stat[5])
		statFin.append(stat[1])
		statFin.append(stat[2])
		statFin.append(stat[3])
		statFin.append(stat[0])
	
	elif clas == "Rogue":
		statFin.append(stat[1])
		statFin.append(stat[4])
		statFin.append(stat[0])
		statFin.append(stat[3])
		statFin.append(stat[2])
		statFin.append(stat[5])
	
	elif clas == "Sorcerer":
		statFin.append(stat[0])
		statFin.append(stat[4])
		statFin.append(stat[3])
		statFin.append(stat[2])
		statFin.append(stat[1])
		statFin.append(stat[5])
	
	elif clas == "Wizard":
		statFin.append(stat[0])
		statFin.append(stat[4])
		statFin.append(stat[3])
		statFin.append(stat[5])
		statFin.append(stat[1])
		statFin.append(stat[2])
	else:
		statFin=stat
	
	return statFin
	
def statAdd(stat1,stat2):
	global race
	statFin = []
	for i in range(6):
		statFin.append(stat1[i] + stat2[i])
	if race == "HalfOrc":
		if statFin[3] < 3:
			statFin[3] = 3
	return statFin

def textAdd(stat):
	statFin = []
	statFin.append("Str: "+str(stat[0]))
	statFin.append("Dex: "+str(stat[1]))
	statFin.append("Con: "+str(stat[2]))
	statFin.append("Int: "+str(stat[3]))
	statFin.append("Wis: "+str(stat[4]))
	statFin.append("Cha: "+str(stat[5]))
	
	return statFin

def printChar():
	global classList, stats, charStats, clas, align, race2, trait1, trait2

	#if save:
	#	chartxt = open("chartxt.txt", "a")
	#	chartxt.write("-------------------------\n")
	#	chartxt.write("Alignment: " + align + "\n")
	#	chartxt.write("Race: " + race2 + "\n")
	#	chartxt.write("Class: " + clas + "\n")
	#	chartxt.write("Traits: " + trait1 + ", " + trait2 + "\n")
	#	chartxt.write("Stats: " + str(textAdd(statAdd(charStats,clasAdd(stats,clas)))) + "\n") # Takes the random stats and changes the order to fit the class, adds the race bonuses, and adds text for readability.
	#
	#else:
	
#	flask.flash("Alignment: \n\t" + align + "\nRace: \n\t" + race2 + "\nClass: \n\t" + clas + "\nTraits: \n\t" + trait1 + ", " + trait2 + "\nStats: \n\t" + str(textAdd(statAdd(charStats,clasAdd(stats,clas)))))

	Details = [{'Field':"Alignment:", 'Value':align}, {'Field':"Race:", 'Value':race2}, {'Field':"Class:", 'Value':clas}, {'Field':"Traits:", 'Value':trait1 + ", " + trait2}, {'Field':"Stats:", 'Value':str(textAdd(statAdd(charStats,clasAdd(stats,clas))))}]
#	flask.flash("Alignment: \n\t" + align + "\nRace: \n\t" + race2 + "\nClass: \n\t" + clas + "\nTraits: \n\t" + trait1 + ", " + trait2 + "\nStats: \n\t" + str(textAdd(statAdd(charStats,clasAdd(stats,clas)))))
	flask.flash(Details)
	
	classList.append(clas)
	
	if len(classList)%classCount == 0:
		classList = []

def start(party,reroll):
	global race3

	if is_number(party):
		party = int(party)
		if party < 0:
			party = abs(party)
			for i in range(int(party)):
				race3 = "skeleton"
				main(reroll)
		elif party == 420:
			party = 1
			for i in range(int(party)):
				race3 = "Turtle"
				main(reroll)
		else:
			race3 = "none"
			for i in range(int(party)):
				main(reroll)
	else:
		race3 = "none"
		main(reroll)

										# This asks for the size of the party
#party = raw_input("Generate how many characters? (There are "+str(classCount)+" different class options)\n")
										# This askes for if the user wants to reroll stats under 10 or not
#reroll = raw_input("Re-Roll Stats under 10? (leave blank if no)\n")
										# The party size is then used to generate however many characters
										# Neat feature, will remove for webapp probably
#save = raw_input("Save to text file? (Leave blank for no)\n")
#if is_number(party):
#	for i in range(int(party)):
#		if i%classCount == 0:
#			classList = []
#		main(reroll,save)
#else:
#	main(reroll,save)
