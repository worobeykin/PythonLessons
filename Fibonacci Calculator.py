#Fibonacci Calculator App

print("Welcome to the Fibonacci Calculator App")


#first part of code
amount = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
print("\nThe first " + str(amount) + " numbers of the Fibonacci sequence are:")
f_sequence = [1, 1]
print(type(f_sequence))
for i in range(amount-2):
    x1 = f_sequence[i] + f_sequence[i+1] 
    f_sequence.append(x1)



print('\n'.join(str(value) for value in f_sequence))
#print('\n'.join(map(str, f_sequence)))

#second part of code
print("\nThe Golden Ratio values are:")

values = []
for i in range(len(f_sequence)-1):
    x2 = f_sequence[i+1] / f_sequence[i]
    values.append(x2)
print('\n'.join(map(str, values)))
