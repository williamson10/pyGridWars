import functions

def controls():
	print('Move \t Look \t Quit')
	action = input();
	if action == 'move':
		print('north \t east \t south \t west')
		direction = input();
		if direction == 'north':
			ynum = functions.yToNumber(settings.ypos) -1
			settings.ypos = functions.yToLetter(ynum)
			settings.location = settings.ypos + str(settings.xpos)
		if direction == 'east':
			settings.xpos = settings.xpos + 1
			settings.location = settings.ypos + str(settings.xpos)
		if direction == 'south':
			ynum = functions.yToNumber(settings.ypos) + 1
			settings.ypos = functions.yToLetter(ynum)
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
	