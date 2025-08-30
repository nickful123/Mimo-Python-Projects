####################### Imports #############################

import random

####################### Global Variables ####################

player_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]

####################### Main Game Loop ######################

while player_wins < 2 and computer_wins < 2:
  print()
  print (f"Player won: {player_wins} and Computer won: {computer_wins}")
  print()

  ####################### Variables ###########################

  computer_choice = random.choice(choices)
  players_choice = ""
  winner = ""

  ####################### Game begins #########################

  print("Let's play rock, paper, or scissors")

  #Player inputs their choice
  while players_choice not in ["rock", "paper", "scissors"]:
    players_choice = input("First choose rock, paper, or scissors: ").lower()
    if players_choice not in ["rock", "paper", "scissors"]:
      print ("Please enter a valid option")
      print()
      
  #Game prints computer's choice
  print()
  print(f"Computer chose: {computer_choice}")

  ######################### Game ##############################

  if (players_choice == "rock" and computer_choice == "scissors") or   (players_choice == "scissors" and computer_choice == "paper") or (players_choice  == "paper" and computer_choice == "rock"):
    winner = "Player"

  elif (players_choice == computer_choice):
    winner = "Tie"

  else:
    winner = "Computer"

  ##################### Results ###############################

  if winner == "Player":
    player_wins += 1
    print("You won")

  elif winner == "Computer":
    computer_wins += 1
    print("Computer won")

  else:
    print("It's a tie")

#######################Final Score ############################

print()

if player_wins > computer_wins:
  print("Congratulations! You won.")
else:
  print("Computer won!")
print (f"Player won: {player_wins} and Computer won: {computer_wins}")
