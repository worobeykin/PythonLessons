#The Python Calculator App

def add(a, b):
    """Sum between a and b and return the summation"""
    summation = round(a + b, 4)
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(summation))
    return str(a) + " + " + str(b) + " = " + str(summation)

def subtract(a, b):
    """Subtraction between a and b and return the difference"""
    difference = round(a - b, 4)
    print("The difference of " + str(a) + " and " + str(b) + " is " + str(difference))
    return str(a) + " - " + str(b) + " = " + str(difference)

def multiply(a, b):
    """Multiplication between a and b and return the multiplication result"""
    result_mult = round(a * b, 4)
    print("The difference of " + str(a) + " and " + str(b) + " is " + str(result_mult))
    return str(a) + " * " + str(b) + " = " + str(result_mult)

def divide(a, b):
    """Separation between a and b and return the divide result"""
    if b != 0:
        result_divide = round(a / b, 4)
        print("The difference of " + str(a) + " and " + str(b) + " is " + str(result_divide))
        return str(a) + " / " + str(b) + " = " + str(result_divide)
    else:
        print("You cannot divide by zero")
        return "DIV ERROR"

def exponent(a, b):
    """Exponentiation between a and b and return the exponentiation result"""
    result_exp = round(a ** b, 4)
    print("The result of " + str(a) + " raised to the " + str(b) + " is " + str(result_exp))
    return str(a) + " ** " + str(b) + " = " + str(result_exp)


#Main code
print("Welcome to the The Python Calculator App")

history = []
flag = True

while flag:
    num_1 = float(input("\nEnter a number: "))
    num_2 = float(input("Enter a number: "))
    choice = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").strip().lower()
    if choice == 'addition' or choice == 'a':
        history.append(add(num_1, num_2))
    elif choice == 'subtraction' or choice == 's':
        history.append(subtract(num_1, num_2))
    elif choice == 'multiplication' or choice == 'm':
        history.append(multiply(num_1, num_2))
    elif choice == 'division' or choice == 'd':
        history.append(divide(num_1, num_2))
    elif choice == 'exponentiation' or choice == 'e':
        history.append(exponent(num_1, num_2))
    else:
        history.append("OPP ERROR")
        print("OPP ERROR")

    end_the_program = input("\nWould you like to run the program again (y/n): ").strip().lower()
    if end_the_program != 'y':
        break

print("Calculation Summary:")
for i in history:
    print(i)
print("\nGoodbay")
        

        








    
