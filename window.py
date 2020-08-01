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

def generate_char():
	global party, reroll
	character_return = ""
	#print(dnd_main.start(party.get(), reroll.get(), "local"))
	for i in range(is_number(party.get())):
	#	dnd_main.localstart("1", reroll.get(), "local")
		character = dnd_main.localstart("1", reroll.get(), "local")
		character_return += f"{character[0]['Value']}, {character[1]['Value']}, {character[2]['Value']}\nYour Stats are:\n{character[6]['Value']}\n{character[7]['Value']}\n{character[8]['Value']}\n{character[9]['Value']}\n{character[10]['Value']}\n{character[11]['Value']}\n~~~~~~~~~~\n"
	output.insert(END,character_return)

##Establish Variables
#Create Window and Label it
window = tk.Tk()
window.geometry("500x400")
Title = tk.Label(text="DND Character Randomizer")
output = scrolledtext.ScrolledText(window,wrap=tk.WORD,width=400,height=150,font=("Arial",10))
outputlbl = tk.Label(text="Results:")
##Create User Input Fields
#Party Size
partylbl = tk.Label(text="How large is the party")
party = tk.Entry(relief=tk.SUNKEN)
party.insert(0,'1')

#Yes or No
rerolllbl = tk.Label(text="Re-Roll Stats under 10?")
reroll = tk.Entry(relief=tk.SUNKEN)
reroll.insert(0,'yes')

#Generate Button
generate = tk.Button(relief=tk.RAISED, text="Generate",command=generate_char)

#Pack Fields
Title.pack()
partylbl.pack()
party.pack()
rerolllbl.pack()
reroll.pack()
generate.pack()
outputlbl.pack()
output.pack()

#Open Window
window.mainloop()