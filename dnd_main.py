##Alec Davidson - Summer 2014

import statNumb, dndcharacter, flask

stats = []
charStats = [0,0,0,0,0,0]
classList = []
#classCount = dndcharacter.classCount()
race = clas = traitlist = []
race2 = align = trait1 = trait2 = trait3 = highConcept = trouble = greatSkill = goodSkill = fairSkill = averageSkill = poorSkill = ""
race3 = "none"

def main(reroll,fate):
	reset(fate)
	global race
	for i in range(6):
		stats.append(statNumb.statRand(reroll))
	
	#classCheck()
	
	traitCheck()
	
	printChar(fate)

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def reset(fate):
	global stats, charStats, race, race2, clas, align, traitList, trait1, trait2, trait3, highConcept, trouble, greatSkill, goodSkill, fairSkill, averageSkill, poorSkill
	
	race = dndcharacter.getRace()
	#if race3 == "none":
	#	race = dndcharacter.getRace()
	#else:
	#	race[0] = race3
	stats = []
	charStats = race[1]
	clas = dndcharacter.getClass()
	align = dndcharacter.getAlign(clas[0])
	race2 = race[0]
	traitList = []
	trait1 = dndcharacter.getTrait('archetype')
	trait2 = dndcharacter.getTrait('trope')
	trait3 = dndcharacter.getTrait('traits')
	highConcept = dndcharacter.getTrait('HighConcepts')
	trouble = dndcharacter.getTrait('Trouble')
	greatSkill = dndcharacter.getTrait('Skills')
	goodSkill = dndcharacter.getTrait('Skills')
	fairSkill = dndcharacter.getTrait('Skills')
	averageSkill = dndcharacter.getTrait('Skills')
	poorSkill = dndcharacter.getTrait('Skills')

#def classCheck():
#	global classList, clas
#	if clas in classList:
#		clas = dndcharacter.getClass()
#		classCheck()

def traitCheck():
	global traitList, greatSkill, goodSkill, fairSkill, averageSkill, poorSkill

	global traitList, trait1, trait2, trait3, highConcept, trouble, greatSkill, goodSkill, fairSkill, averageSkill, poorSkill
	
	traitList.append(trait1)
	
	while trait2 in traitList:
		trait2 = dndcharacter.getTrait('trope')
	traitList.append(trait2)
	
	while trait3 in traitList:
		trait3 = dndcharacter.getTrait('traits')
	traitList.append(trait3)
	
	while highConcept in traitList:
		highConcept = dndcharacter.getTrait('HighConcepts')
	traitList.append(highConcept)
	
	traitList.append(greatSkill)
	
	while greatSkill in traitList:
		greatSkill = dndcharacter.getTrait('Skills')
	traitList.append(greatSkill)
	
	while goodSkill in traitList:
		goodSkill = dndcharacter.getTrait('Skills')
	traitList.append(goodSkill)
	
	while fairSkill in traitList:
		fairSkill = dndcharacter.getTrait('Skills')
	traitList.append(fairSkill)
	
	while averageSkill in traitList:
		averageSkill = dndcharacter.getTrait('Skills')
	traitList.append(averageSkill)
	
	while poorSkill in traitList:
		poorSkill = dndcharacter.getTrait('Skills')
	traitList.append(poorSkill)
	
def clasAdd(stat,clas):
	stat.sort()
	statFin = [0,0,0,0,0,0]
	statOrder = clas[1]
	
	for i in range(6):
		statFin[i] = stat[statOrder[i]]
	
	return statFin
	
def statAdd(stat1,stat2):
	global race
	statFin = []
	for i in range(6):
		statFin.append(stat1[i] + stat2[i])
	if race[0] == "HalfOrc":
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
	global classList, stats, charStats, clas, align, race2, trait1, trait2, trait3, highConcept, trouble, greatSkill, goodSkill, fairSkill, averageSkill, poorSkill

	if fate=="yes":
		Details = [
		{'Field':"Alignment:", 'Value':align},
		{'Field':"Race:", 'Value':race2},
		{'Field':"Class:", 'Value':clas[0]},
		{'Field':"High Concept:", 'Value':highConcept},
		{'Field':"Trouble:", 'Value':trouble},
		{'Field':'', 'Value':''},
		{'Field':"Great Skill (+4):", 'Value':greatSkill},
		{'Field':"Good Skill (+3):", 'Value':goodSkill},
		{'Field':"Fair Skill (+2):", 'Value':fairSkill},
		{'Field':"Average Skill (+1):", 'Value':averageSkill},
		{'Field':"Poor Skill (-1)", 'Value':poorSkill},
		{'Field':"", 'Value':''},
		{'Field':"", 'Value':align + ', ' + race2 + ' ' + clas[0] + '. ' + highConcept + ' but ' + trouble + '.'}]
	else:
		StatListing = textAdd(statAdd(charStats,clasAdd(stats,clas)))
		Details = [
		{'Field':"Alignment:", 'Value':align},
		{'Field':"Race:", 'Value':race2},
		{'Field':"Class:", 'Value':clas[0]},
		{'Field':"Traits:", 'Value':trait1},
		{'Field':"", 'Value':trait2},
		{'Field':"", 'Value':trait3},
		{'Field':"Stats:", 'Value':StatListing[0]},
		{'Field':"", 'Value':StatListing[1]},
		{'Field':"", 'Value':StatListing[2]},
		{'Field':"", 'Value':StatListing[3]},
		{'Field':"", 'Value':StatListing[4]},
		{'Field':"", 'Value':StatListing[5]},
		{'Field':"", 'Value':align + ', ' + race2 + ' ' + clas[0] + '. ' + trait1 + ', ' + trait2 + ', and ' + trait3 + '.'}]
	
	flask.flash(Details)
	
	classList.append(clas)
	
	#if len(classList)%classCount == 0:
	#	classList = []

def start(party, reroll, fate):
	global race3

	if is_number(party):
		party = int(party)
	else:
		race3 = "none"
		party = 1
	
	if party < 0:
		party = abs(party)
		
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
