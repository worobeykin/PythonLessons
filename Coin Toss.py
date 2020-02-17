#Coin Toss App

import random
print("Welcome to the Coin toss App")

heads = 0
tails = 0

print("\nI will flip a coin a set number of times.")
amount = int(input("How many times would you like to flip: "))

accept = input("Would you like to see the result(y/n): ").lower()
print("\nFlipping...")

for i in range(amount):
    itera = random.randint(0,1)
    if accept.startswith('y'):
        print(str(itera))
    if itera == 0:
        heads += 1
    else:
        tails +=1
    if heads == tails:
        print("At " + str(i+1) + " flips, operation at " + str(int((i+1)/2)))


print("\nResults of flipping a coin " + str(amount) + " times:\n")
print("Side\t" + "Count\t" + "Percentage")
print("0\t" + str(heads) + "/" + str(amount) + "\t" + str(round(heads*100/amount, 2)) + "%")
print("1\t" + str(tails) + "/" + str(amount) + "\t" + str(round(tails*100/amount, 2)) + "%")
        
