#RockPaperScissors

import random

print("Welcome to a game of Rock, Paper, Scissors")
rounds = int(input("\nHow many rounds would you like to play: "))
moves = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

for i in range(rounds):
    print("\nRound " + str(i+1) + "\nPlayer: " + str(player_score) + "\tComputer: " + str(computer_score))

    rand_variat = random.randint(0, 2)
    index = moves[rand_variat]

    player_variant = input("Time to pick...rock, paper, scissors: ").lower()

    if player_variant not in moves:
        computer_score +=1
        print("there is not in list, computer +1")
        continue

    if player_variant != index:
        print("\tComputer: " + str(index))
        print("\tPlayer: " + str(player_variant))
        if player_variant == 'rock' and index == 'scissors':
            print("\trock win scissors")
            player_score +=1
        if player_variant == 'paper' and index == 'rock':
            print("\tPaper covers rock")
            player_score +=1
        if player_variant == 'scissors' and index == 'paper':
            print("\tScissors win paper")
            player_score +=1

        if player_variant == 'rock' and index == 'paper':
            print("\paper win rock")
            computer_score +=1
        if player_variant == 'paper' and index == 'scissors':
            print("\tScissors win paper")
            computer_score +=1
        if player_variant == 'scissors' and index == 'rock':
            print("\trock win Scissors")
            computer_score +=1        
    else:
        print("\tComputer: " + str(index))
        print("\tPlayer: " + str(player_variant))
        print("\tIt is a tia, how boring!")
        print("\tThis round was a tia!")

print("\nFinal Game Results")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(player_score))
print("\tComputer Score: " + str(computer_score))
if player_score > computer_score:
    print("\tWinner: PLAYER!!!")
if player_score < computer_score:
    print("\tWinner: Computer!!!")
if player_score == computer_score:
    print("\tNichy!!!")
          
    
    
