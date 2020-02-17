#Factorial Calculator App
import math

print("Welcome to the Factorial Calculator App")

number = int(input("What number would you like to enter: "))

fac = 1
list_numbers = str(number) + "!="
for i in range(1, number+1):
    list_numbers += str(i) + "*"
    fac *= i
print(list_numbers[0:-1])

print(str(number) + "!=", end="")
for i in range(1, number):
    print(str(i), end="*")
print(str(number))
    

print("\nHere is the result from math library:")
print("The factorial of " + str(number) + " is " + str(math.factorial(number)))


print("\nHere is the result from own method:")
print("The factorial of " + str(number) + " is " + str(fac))
