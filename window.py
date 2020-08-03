#Imports
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
import dnd_main

#Establish Functions
def is_number(s):
	try:
		int(s)
		return int(s)
	except ValueError:
		return 1

def generate_char_yes():
	global party
	character_return = ""
	#print(dnd_main.start(party.get(), reroll.get(), "local"))
	for i in range(is_number(party.get())):
	#	dnd_main.localstart("1", reroll.get(), "local")
		character = dnd_main.localstart("1", "yes", "local")
		character_return += f"{character[0]['Value']}, {character[1]['Value']}, {character[2]['Value']}\nYour rerolled Stats are:\n{character[6]['Value']}\n{character[7]['Value']}\n{character[8]['Value']}\n{character[9]['Value']}\n{character[10]['Value']}\n{character[11]['Value']}\nTraits include '{character[3]['Value']}' and '{character[4]['Value']}'\n~~~~~~~~~~\n"
	output.insert(END,character_return)

def generate_char_no():
	global party
	character_return = ""
	#print(dnd_main.start(party.get(), reroll.get(), "local"))
	for i in range(is_number(party.get())):
	#	dnd_main.localstart("1", reroll.get(), "local")
		character = dnd_main.localstart("1", "no", "local")
		character_return += f"{character[0]['Value']}, {character[1]['Value']}, {character[2]['Value']}\nYour Stats are:\n{character[6]['Value']}\n{character[7]['Value']}\n{character[8]['Value']}\n{character[9]['Value']}\n{character[10]['Value']}\n{character[11]['Value']}\nTraits include '{character[3]['Value']}' and '{character[4]['Value']}'\n~~~~~~~~~~\n"
	output.insert(END,character_return)

##Establish Variables
#Create Window and Label it
window = tk.Tk()
window.geometry("500x400")
topframe = Frame(window)
topframe.pack(side="top")
midframe = Frame(window)
midframe.pack()
botframe = Frame(window)
botframe.pack(side="bottom")
Title = tk.Label(topframe, text="DND Character Randomizer")
outputlbl = tk.Label(botframe, text="Results:")
output = scrolledtext.ScrolledText(botframe, wrap=tk.WORD,width=400,height=150,font=("Arial",10))
##Create User Input Fields
#Party Size
partylbl = tk.Label(topframe, text="How large is the party")
party = tk.Entry(topframe, relief=tk.SUNKEN)
party.insert(0,'1')

#Yes or No
rerolllbl = tk.Label(topframe, text="Re-Roll Stats under 10?")
reroll = tk.Button(midframe, relief=tk.RAISED, text="Yes",command=generate_char_yes)
noroll = tk.Button(midframe, relief=tk.RAISED, text="No",command=generate_char_no)

#Pack Fields
Title.pack(side="top")
partylbl.pack(side="top")
party.pack(side="top")
rerolllbl.pack(side="top")
reroll.pack(side="left")
noroll.pack(side="right")
outputlbl.pack()
output.pack(side="bottom")

#Open Window
print("You can minimize this window, but do not close!")
window.mainloop()
