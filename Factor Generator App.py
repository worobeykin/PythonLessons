#Factor Generator App

print("Welcome to the Factor Generator App")

flag = True

while flag:
    number = int(input("\nEnter number: "))
    factors = []
    for i in range(1, number+1):
        if (number % i) == 0:
            factors.append(i)
    print("\nFactors of " + str(number) + " are:\n")
    for i in factors:
        print(i)
    print("\nIn summary:")
    for i in range(int(len(factors)/2)):
        multiply = factors[i] * factors[-i-1]
        print(str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(multiply))
    choice = input("\nRun again (y/n): ")
    if choice != 'y':
        print("Goodbay")
        flag = False
    
        
         
