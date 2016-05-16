#! /usr/bin/python3
import settings, functions, json, os, controls
from functions import bcolors


#initialize global variables
settings.int()


#open grid file
with open('locations.json') as data_file:
	data = json.load(data_file)

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

#inital player setup
print('enter your name')
settings.name = input()
os.system('cls' if os.name == 'nt' else 'clear')

#welcome the player
banner = settings.name +" " + str(settings.health) + " health"
print(banner)
settings.location = 'a1'
print('Welcome to GridWars')
print('You open your eyes for the first time in 3 years. You cant remeber anything but you can hear the faint sounds of a battle in the distance')
print('hit enter to continue') 
pause = input()

#start game loop
while True: 
	os.system('cls' if os.name == 'nt' else 'clear')
	settings.health = settings.health + data[settings.location]['health']
	if settings.health < 1:
		print('you dead!')
		quit()
	functions.showPlayerInfo()
	print(data[settings.location]['description'])
	print()
	print()
	#print(bcolors.FAIL, 'debug')
	#print(bcolors.FAIL, 'LOCATION: ', settings.location, bcolors.ENDC)
	#print("data['locations'][" + str(settings.location) + "]['description']")
	#print(len(data['locations']))
	print(settings.message)
	settings.message = ''
	functions.controls()
