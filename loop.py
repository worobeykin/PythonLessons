#Loop

teams = ["giants", "bills", "jets", "patriots"]
for i in range(5, 10, 2):
    print(i)

print(teams)
print(type(teams))

for i in teams:
    print(i.title())


values = [1,2,3,4,5,]
total_sum = 0
for value in values:
    total_sum += value
print(total_sum)

triples = [["a", "b", "c"], ["1", "2", "3"], ['do', "re", "me"]]
for list_value in triples:
    print(list_value)
for list_value in triples:
    for element in list_value:
        print(element, end=' ')

print("\n")
for i in range(1,31):
    print(i, end=' ')

word = "Hello World"
list_word = list(word)
print(word)
print(list_word)

new_word = " ".join(list_word)
print(list_word)
print(new_word)

numbers = list(range(1,10,1))
cubes = [i**3 for i in numbers]
print(cubes)
for cube in cubes:
    print(cube)

#new modul
    
numbers = list(range(1,11))
print("\nSlicing")
for num in numbers[0:5]:
    print(num)


new_numbers = numbers.copy()
print(numbers)
print(new_numbers)

numbers.pop()

print(numbers)
print(new_numbers)


names = ["jack", "mark", "Smith"]
age = [9, 7, 16, 20]

#for i in range(len(names)):
#    print(names[i].title() + ": " + str(age[i]))

for name, age in zip(names,age):
    print(name.title() + ": " + str(age))












    
