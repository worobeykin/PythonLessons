#Grocery List App

import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print("Welcome to the Grocery List App")
print("Current Date and Time: " + day + "/" + month + " " + hour + ":" + minute)
print("You currently have Meat and cheese in your list.")

grocery_list = ["Meat", "Cheese"]

#add food
food = input("\nType of food to add to the grocery list: ")
grocery_list.append(food.title())
food = input("\nType of food to add to the grocery list: ")
grocery_list.append(food.title())
food = input("\nType of food to add to the grocery list: ")
grocery_list.append(food.title())

print("\nHere is your grocery list:")
print(str(grocery_list))

#sort
grocery_list.sort()
print("\nHere is your grocery list sorted:")
print(grocery_list)


#purchase
print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
bought_item = input("What food did your just buy: ").title()
grocery_list.remove(bought_item)
print("Removing " + str(bought_item) + " from list")
print(grocery_list)

print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
bought_item = input("What food did your just buy: ").title()
grocery_list.remove(bought_item)
print("Removing " + str(bought_item) + " from list")
print(grocery_list)

print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)
bought_item = input("What food did your just buy: ").title()
grocery_list.remove(bought_item)
print("Removing " + str(bought_item) + " from list")
print(grocery_list)

print("\nCurrent grocery list: " + str(len(grocery_list)) + " items")
print(grocery_list)


no_item = grocery_list.pop()
print("\nSorry, the store is out of " + no_item)
new_food = input("What food would you like instead list: ").title()
grocery_list.insert(0, new_food)

print("new list: " + str(grocery_list))






