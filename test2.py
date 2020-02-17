# Letter Counter App

print("Letter Counter App")

name = input("\nWhat is your name:").title().strip()
print("Hello " + name + "!")

print("I will count the number of times")
message = input("\nWhat is the messade:")
letter = input("\nWhat should we find and count:")

#standardize to lower case
message = message.lower()
letter = letter.lower()

#get the count and display results
letter_count = message.count(letter)
print("\n" + name + ", your massage has " + str(letter_count) + " " + letter + "'s in it")
