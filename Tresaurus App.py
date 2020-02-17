#Tresaurus App

import random

thresaurus = {
    "hot":['balmy','summery','tropical','scorching'],
    "cold":['chilly','cool','freezing','frigid','polar'],
    "happy":['content','cheery','merry','jovial','jocular'],
    "sad":['unhappy','downcast','miserable','glum','melancholy'],
    }

print("Welcome to the tresaurus App")

print("\nWe have four words:\n")
#for key, values in thresaurus.items():
#    print("\t-" + str(key))

for key in thresaurus.keys():
    print("\t-" + str(key))

word = input("\nWhat word you would like to get a synonym for: ").lower().strip()

if word in thresaurus.keys():
    index = random.randint(0, 3)
    print("\nThe synonym for " + word + " is " + thresaurus[word][index])
          

else:
    print("-")
