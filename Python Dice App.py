#Python Dice App
import random

def simulate_dice(side=1, dice=1):
    """Simulate values in our dise plaing"""
    print("\n-----Results are as followed-----\t")
    amount = 1
    sum_value = 0
    while amount <= dice:    
        side_i = random.randint(1, side)
        amount +=1
        sum_value += side_i
        print("\t" + str(side_i))
    print("The total value of your roll is " + str(sum_value))

print("Welcome to the Python Dice App")

#Main part of program
playing = True
while playing:
    sides_amount = int(input("\n How many sides would you like on your dice: "))
    dice_amount = int(input("\n How many dice would you like to roll: "))

    simulate_dice(sides_amount, dice_amount)

    choice = input("\n Would you like to roll again (y/n): ").strip().lower()
    if choice == 'y':
        continue
    else:
        print("\nGoodbay")
        playing = False
        

