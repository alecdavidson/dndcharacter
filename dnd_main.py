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
traitList = []
trait1 = ""
trait2 = ""
highConcept = ""
trouble = ""
greatSkill = ""
goodSkill = ""
fairSkill = ""
averageSkill = ""

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

def reset(fate):
	global stats, charStats, race, race2, clas, align, traitList, trait1, trait2, highConcept, trouble, greatSkill, goodSkill, fairSkill, averageSkill
	
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
	traitList = []
	trait1 = dndcharacter.getTrait('traits')
	trait2 = dndcharacter.getTrait('traits')
	highConcept = dndcharacter.getTrait('HighConcepts')
	trouble = dndcharacter.getTrait('Trouble')
	greatSkill = dndcharacter.getTrait('Skills')
	goodSkill = dndcharacter.getTrait('Skills')
	fairSkill = dndcharacter.getTrait('Skills')
	averageSkill = dndcharacter.getTrait('Skills')
	
def traitCheck():
	global traitList, trait1, trait2, highConcept, trouble, greatSkill, goodSkill, fairSkill, averageSkill
	
	traitList.append(trait1)
	
	while trait2 in traitList:
		trait2 = dndcharacter.getTrait('traits')
	traitList.append(trait2)
	
	while highConcept in traitList:
		highConcept = dndcharacter.getTrait('HighConcepts')
	traitList.append(highConcept)
	
	while trouble in traitList:
		trouble = dndcharacter.getTrait('Trouble')
	traitList.append(trouble)
	
	while greatSkill in traitList:
		greatSkill = dndcharacter.getTrait('Convictions')
	traitList.append(greatSkill)
	
	while goodSkill in traitList:
		goodSkill = dndcharacter.getTrait('Expertise')
	traitList.append(goodSkill)
	
	while fairSkill in traitList:
		fairSkill = dndcharacter.getTrait('Expertise')
	traitList.append(fairSkill)
	
	while averageSkill in traitList:
		averageSkill = dndcharacter.getTrait('Expertise')
	traitList.append(averageSkill)
	

race2 = race
race = race2.replace("-","")

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

def main(reroll,fate):
	reset(fate)
	global race
	for i in range(6):
		stats.append(statNumb.statRand(reroll))
	
	classCheck()
	
	traitCheck()
	
	raceStat(race)
	
	printChar(fate)

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

def printChar(fate):
	global classList, stats, charStats, clas, align, race2, trait1, trait2, highConcept, trouble, greatSkill, goodSkill, fairSkill, averageSkill

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
	if fate=="yes":
		Details = [
		{'Field':"Alignment:", 'Value':align},
		{'Field':"Race:", 'Value':race2},
		{'Field':"Class:", 'Value':clas},
		{'Field':"High Concept:", 'Value':highConcept},
		{'Field':"Trouble:", 'Value':trouble},
		{'Field':"Great Skill (+4):", 'Value':greatSkill},
		{'Field':"Good Skill (+3):", 'Value':goodSkill},
		{'Field':"Fair Skill (+2):", 'Value':fairSkill},
		{'Field':"Average Skill (+1):", 'Value':averageSkill},
		{'Field':'', 'Value':''},
		{'Field':'', 'Value':''}]
	else:
		StatListing = textAdd(statAdd(charStats,clasAdd(stats,clas)))
		Details = [
		{'Field':"Alignment:", 'Value':align},
		{'Field':"Race:", 'Value':race2},
		{'Field':"Class:", 'Value':clas},
		{'Field':"Traits:", 'Value':trait1},
		{'Field':"", 'Value':trait2},
		{'Field':"Stats:", 'Value':StatListing[0]},
		{'Field':"", 'Value':StatListing[1]},
		{'Field':"", 'Value':StatListing[2]},
		{'Field':"", 'Value':StatListing[3]},
		{'Field':"", 'Value':StatListing[4]},
		{'Field':"", 'Value':StatListing[5]}]
	
	
#	flask.flash("Alignment: \n\t" + align + "\nRace: \n\t" + race2 + "\nClass: \n\t" + clas + "\nTraits: \n\t" + trait1 + ", " + trait2 + "\nStats: \n\t" + str(textAdd(statAdd(charStats,clasAdd(stats,clas)))))
	flask.flash(Details)
	
	classList.append(clas)
	
	if len(classList)%classCount == 0:
		classList = []

def start(party,reroll,fate):
	global race3

	if is_number(party):
		party = int(party)
	else:
		race3 = "none"
		party = 1
	
	if party < 0:
		party = abs(party)
		for i in range(int(party)):
			race3 = "skeleton"
			main(reroll,fate)
	elif party == 420:
		party = 1
		for i in range(int(party)):
			race3 = "Turtle"
			main(reroll)
	else:
		race3 = "none"
		for i in range(int(party)):
			main(reroll,fate)

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
