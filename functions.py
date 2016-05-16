import os
import settings

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def yToNumber(myletter):
	return ord(myletter) - 97

def yToLetter(mynumber):
	return chr(mynumber + 97)

def showPlayerInfo():
	if settings.health > 50:
		color = bcolors.OKGREEN
	elif settings.health < 25:
		color = bcolors.FAIL
	else:
		color = bcolors.WARNING
	display = bcolors.OKBLUE + settings.name + '\t' + color + 'Health:'+ str(settings.health) + bcolors.ENDC + '\n'
	print(display)

def controls():
	print('Move \t Look \t Quit')
	action = input();
	if action == 'move':
		print('north \t east \t south \t west')
		direction = input();
		if direction == 'north':
			ynum = yToNumber(settings.ypos) -1
			settings.ypos = yToLetter(ynum)
			settings.location = settings.ypos + str(settings.xpos)
		if direction == 'east':
			settings.xpos = settings.xpos + 1
			settings.location = settings.ypos + str(settings.xpos)
		if direction == 'south':
			ynum = yToNumber(settings.ypos) + 1
			settings.ypos = yToLetter(ynum)
			settings.location = settings.ypos + str(settings.xpos)
		if direction == 'west':
			settings.xpos = settings.xpos - 1
			settings.location = settings.ypos + str(settings.xpos)
	elif action == 'quit':
		os.system('cls' if os.name == 'nt' else 'clear')
		print('see ya later')
		quit()

	elif action == 'look':
		settings.message = 'Nothing to see here. Move along!'	
	
	elif (action != 'look') or (action != 'quit') or (action != 'move'):
		settings.message = 'Nothing to do Abe!'
	
