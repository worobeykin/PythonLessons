#Factor Generator App

print("Welcome to the Factor Generator App")

flad = True

while flag:
    number = int(input("Enter number: "))
    factors = []
    for i in range(number):
        if number % i == 0:
            factors.append(i)
            print(factors)
            
