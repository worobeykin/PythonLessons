#Voter Registration App

print("Welcome to the Voter registration App\n")

name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']

if age < 18:
    print("\nYou are not old enough to register to vote.")
elif age >= 18:
    print("\nCongretulations " + name + "! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")
    print("\t-" + str("\n\t-".join(parties)))
    party = input("\nWhat party would you like to join: ").title()
    if party in parties:
        print("\nCongratulations " + name + "! You have joind the " + party + " party!")

#        for i in parties:
        if party == "Republican" or party == "Democratic":
            print("That is a major party!")
             
        elif party == "Independent":
            print("You are independant person!")
               
        else:
            print("Your party is not a major party!")
             
                
            

    else:
        print("\nThe party you chose is not given party.")
    
