#Teachers App

print("Welcome to the favorite teachers program")

Fteachers = []

#Input
teacher = input("\nWho is your first favorite teacher:").title()
Fteachers.append(teacher)
teacher = input("Who is your second favorite teacher:").title()
Fteachers.append(teacher)
teacher = input("Who is your third favorite teacher:").title()
Fteachers.append(teacher)
teacher = input("Who is your forth favorite teacher:").title()
Fteachers.append(teacher)

print("\nYour favorite teachers are: " + str(Fteachers))
print("Your favorite teachers alphabetically are: " + str(sorted(Fteachers)))
print("Your favorite teachers in reverce alphabetically are: " + str(sorted(Fteachers, reverse=True)))
print("\nYour top two favorite teachers are: " + str(Fteachers[0]) + " and " + str(Fteachers[1]))
print("Your next two favorite teachers are: " + str(Fteachers[2]) + " and " + str(Fteachers[3]))
print("Your last favorite teachers is: " + str(Fteachers[len(Fteachers)-1]))
print("You have " + str(len(Fteachers)) + " favorite teachers")

#second part of program

teacher = input("\nOops, " + str(Fteachers[0]) + " is not your favorite teacher now.\t Who will be next:").title()
Fteachers.insert(0, teacher)

print("\nYour favorite teachers are: " + str(Fteachers))
print("Your favorite teachers alphabetically are: " + str(sorted(Fteachers)))
print("Your favorite teachers in reverce alphabetically are: " + str(sorted(Fteachers, reverse=True)))
print("\nYour top two favorite teachers are: " + str(Fteachers[0]) + " and " + str(Fteachers[1]))
print("Your next two favorite teachers are: " + str(Fteachers[2]) + " and " + str(Fteachers[3]))
print("Your last favorite teachers is: " + str(Fteachers[len(Fteachers)-1]))
print("You have " + str(len(Fteachers)) + " favorite teachers")

#last part

teacher = input("\nYou decide to remove teacer:").title()
Fteachers.remove(teacher)

print("\nYour favorite teachers are: " + str(Fteachers))
print("Your favorite teachers alphabetically are: " + str(sorted(Fteachers)))
print("Your favorite teachers in reverce alphabetically are: " + str(sorted(Fteachers, reverse=True)))
print("\nYour top two favorite teachers are: " + str(Fteachers[0]) + " and " + str(Fteachers[1]))
print("Your next two favorite teachers are: " + str(Fteachers[2]) + " and " + str(Fteachers[3]))
print("Your last favorite teachers is: " + str(Fteachers[len(Fteachers)-1]))
print("You have " + str(len(Fteachers)) + " favorite teachers")

