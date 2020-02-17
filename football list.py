#Football prograb list App

print("Welcome to the football list program")

football_list = []

forward = input("\nWho is your forward:").title()
football_list.append(forward)
halfback = input("\nWho is your halfback:").title()
football_list.append(halfback)
defender = input("\nWho is your defender:").title()
football_list.append(defender)
goalkeeper = input("\nWho is your goalkeeper:").title()
football_list.append(goalkeeper)


print("\n\tYou have " + str(len(football_list)) + " players")
print("\t\tForward:\t" + str(football_list[0]))
print("\t\tHalfback:\t" + str(football_list[1]))
print("\t\tDefender:\t" + str(football_list[2]))
print("\t\tGoalkeeper:\t" + str(football_list[3]))

print("\nOh no, " + defender + " is injured.")
football_list.remove(defender)
print("You have only " + str(len(football_list)) + " players")
defender = input("Who will be new Defender: ").title()
football_list.insert(2,defender)

print("\n\tYou have " + str(len(football_list)) + " players")
print("\t\tForward:\t" + str(football_list[0]))
print("\t\tHalfback:\t" + str(football_list[1]))
print("\t\tDefender:\t" + str(football_list[2]))
print("\t\tGoalkeeper:\t" + str(football_list[3]))

#last program code
print("\nGodd luck " + defender)
print("You have " + str(len(football_list)) + " players")
