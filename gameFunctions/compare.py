from gameFunctions import gameVars

# need a function to run to compare the choices
# figure out what to pass into the function - hink => what are you comparing?
#
def compareChoices(player):
	#always check a breaking condition first
	if player == gameVars.computer:
		#we have a tie, no point in ging any further
		print("\033[1;33;40m tie, no one wins! try again\033[1;37;40m")

	elif player == "quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("\033[0;31;40m You lose!", gameVars.computer, "covers", player, "\033[1;37;40m\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\033[0;32;40m You won!", player, "smashes", gameVars.computer, "\033[1;37;40m\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("\033[0;31;40m You lose!", gameVars.computer, "cuts", player, "\033[1;37;40m\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\033[0;32;40m You won!", player, "covers", gameVars.computer, "\033[1;37;40m\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	
	elif player == "scissors":
		if gameVars.computer == "rock":
			print("\033[0;31;40m You lose!", gameVars.computer, "smashes", player, "\033[1;37;40m\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("\033[0;32;40m You won!", player, "cuts", gameVars.computer, "\033[1;37;40m\n")
			gameVars.computer_lives = gameVars.computer_lives -1
