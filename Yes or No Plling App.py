#Yes or No Plling App

print("Welcome to the Polling App")

issue = input("What issue does we have: ")
voters = int(input("The number of voters: "))
passwd = input("Admin passwors is: ")

yes = 0
no = 0

results = {}

#Simulate the polling process
for i in range(voters):
    full_name = input("\nEnter your full name: ").title()
    if full_name in results.keys():
        print("\nYou can't vote agane.")
        continue
    else:
        print("Today we have the issue: " + issue)
        choice = input("Your choice is(yes/no): ").lower()
        if (choice == 'yes') or (choice == 'y'):
            choice = 'yes'
            yes += 1                       
        elif (choice == 'no') or (choice == 'n'):
            choice = 'no'
            no += 1
        else:
            
            print("Your vone is not yes or no and will not influence the pull")

        results[full_name] = choice
        print("\nThanks for your vote!")

print("\n" + str(len(results)) + " people voted:")
for key in results.keys():
    print(key)

#print("\nAt the end of:\n" + "yes: " + str(yes) + "\nno: " + str(no))
if yes > no:
    print("\nWe win!" + str(yes) + " votes to " + str(no))
elif yes < no:
    print("\nWe loose!" + str(yes) + " votes to " + str(no))
else:
    print("\nIt was a tie!" + str(yes) + " votes to " + str(no))

get_passwd = input("\nTo see all results you can enter the password: ")
if get_passwd == passwd:
    print("\nAll results are:")
    for k, v in results.items():
        print("Voter: " + k + "\tVote: " + v)
else:
    print("Access denied")

print("\nGoodbay")
    


    










        
            
        
