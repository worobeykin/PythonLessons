#Quadratic Equation Solve App

import math
import cmath

print("Welcome to the quadratic Equation Solve App")
print("\nAquadratic equation is of the form ax^2 +bx + c = 0")
print("A complex number has two parts: a +bj")

amount = int(input("\nHow many equations would you like to solve today: "))

for i in range(amount):
    print("\nSolving equation #" + str(i+1) + "\n--------------------------")

    value_a = float(input("Please enter your value of a (coefficient of x^2):"))
    value_b = float(input("Please enter your value of b (coefficient of x):"))
    value_c = float(input("Please enter your value of c (coefficient):"))

    discriminant = float((value_b**2) - (4*value_a*value_c))


    x1 = ((-value_b + cmath.sqrt(discriminant)) / (2*value_a))
    x2 = ((-value_b - cmath.sqrt(discriminant)) / (2*value_a))

    print("\nThe solutions to " + str(value_a) + "x^2 + " +str(value_b) + "x + " + str(value_c) + " = 0 are:")
    print(x1)
    print(x2)

