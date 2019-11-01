# import the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

# adding lives -> when one or the other gets to 0, win/lose
player_lives = 5
computer_lives = 5

# let the AI make a choice
computer=choices[randint(0,2)]

# set up a game loop here so we don't have to keep restarting
player = False

def winorlose(status):
	print("called win or lose function", status, "\n")
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		# reset the game and start all over again
		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
while player is False:
	player=input("choose rock, paper or scissors \n")

	# start doing some logic and condition checking
	print("computer: ", computer, "player: ", player)

	# always check a breaking condition first
	if player == computer:
		#we have a tie, no point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()
		
	else:
		print("NOT a tie. Now we can check other conditions")
		if player == "rock":
			print("check and see what the computer is, and win or lose")
	

