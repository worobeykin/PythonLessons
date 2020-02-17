print("Welcome")

name = input("\nWhat is your name: ").title().strip()
print("Hello, " + name + "!")

print("I will count the number of times.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count: ")

message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)
print("\n" + name + ", ypur massege has " + str(letter_count) + " " + letter + "'s in it.")
