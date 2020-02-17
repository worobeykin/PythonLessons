#Frecuency Analysis App

from collections import Counter

print("Welcome to the Frecuency Analysis App.")

non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',
'.','?','!',',','"',"'",':',';','(',')','%','$','&','#','\n','\t', '-', '-']

#first part
key_phrase_1 = input("\nPlease enter the phrase: ").lower()


for index in key_phrase_1:
    if index in non_letters:
        key_phrase_1 = key_phrase_1.replace(index, '')
        

total_occurrences = len(key_phrase_1)

letter_count = Counter(key_phrase_1)
print("Here is the frequency analysis from key phrase 1: \n")


print("Letter\t\tOccurrence\tPercentage")
for k, v in sorted(letter_count.items()):          
      print(k + "\t\t" + str(v) + "\t\t" + str(round(v*100/total_occurrences, 2)) + "%")

ordered_letter_count = letter_count.most_common()
print("\nLetters ordered from highest occurrence to lowest:")
for i in ordered_letter_count:
    print(i[0], end='')


#second part
key_phrase_2 = input("\n\nPlease enter the phrase: ").lower()


for index in key_phrase_2:
    if index in non_letters:
        key_phrase_2 = key_phrase_2.replace(index, '')
        

total_occurrences = len(key_phrase_2)

letter_count = Counter(key_phrase_2)
print("Here is the frequency analysis from key phrase 1: \n")


print("Letter\t\tOccurrence\tPercentage")
for k, v in sorted(letter_count.items()):          
      print(k + "\t\t" + str(v) + "\t\t" + str(round(v*100/total_occurrences, 2)) + "%")

ordered_letter_count = letter_count.most_common()
print("\nLetters ordered from highest occurrence to lowest:")
for i in ordered_letter_count:
    print(i[0], end='')






            

            

