# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("\033[1;37;40m============================================")
	print("\033[1;36;40m Computer Lives:", gameVars.computer_lives, "/5")
	print("\033[1;35;40m Player Lives:", gameVars.player_lives, "/5")
	print("\033[1;37;40m============================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors \n")
	compare.compareChoices(player)

	# start doing some logic and condition checking
	# print("computer: ", computer, "player: ", player)

	# -- this is where you would do the compare stuff

	# -- end compare stuff

	
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
	
	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]
	

