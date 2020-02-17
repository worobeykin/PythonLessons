#Guess my number App

import random

print("Welcome to the Guess my number App")
name = input("\nHello! What is your name: ").title().strip()
print("Well " + name + ", I am thinking of a number between 1 and 20.")
a = 0
number = random.randint(1,20)

for i in range(5):    
    num = int(input("\nNake a guess: "))
    if num == number:
        print("Good job, " + name + "! You guessed my number in " + str(i+1) + " guesses!")
        a = 1
        break
    elif num > number:
        print("Your guess is too high.")
    elif num < number:
        print("Your guess is too low.")
if a != 1:
    print("loose")
