#Shipping Accounts Program

users = ['eramon', 'footea', 'davisv', 'papinukt', 'allenj', "eramon"]
print("Welcome to the Shipping Accounts Program")

username = str(input("What is your name: ")).lower().strip()

key = False
for user in users:
    
    if user == username:
        print("\nHello " + username + ". Welcom back to your account.")
        print("Current shipping prices are as follows:\n")
        print("Shippig orders 0 to 100:\t $5.10 each")
        print("Shippig orders 100 to 500:\t $5.00 each")
        print("Shippig orders 500 to 1000:\t $4.95 each")
        print("Shippig orders over 1000:\t $4.80 each")
        key = True
        break

if key:
    items = int(input(("How many items would you like to ship: ")))

    if items <= 100:
        costs = round(items*5.10, 3)
        print("To ship " + str(items) + " it will cost you $" + str(costs) + " at $5.10 per item")
    elif items <= 500:
        costs = round(items*5.00, 3)
        print("To ship " + str(items) + " it will cost you $" + str(costs) + " at $5.00 per item")
    elif items <= 1000:
        costs = round(items*4.95, 3)
        print("To ship " + str(items) + " it will cost you $" + str(costs) + " at $4.95 per item")
    elif items > 500:       
        costs = round(items*4.80, 3)
        print("To ship " + str(items) + " it will cost you $" + str(costs) + " at $4.80 per item")
    accept = input("Would you like to bay this oder(y/n): ")
    if accept == 'y':
        print("Okay. Shipping your " + str(items) + " items.")
    else:
        print("Goodbay")
else:
    print("\nAccess denied")


    
    
