#Pythagor teorem App

#Import libraries
import math

#welcome message
print("Welcome to the Right Triangle Solve App")

leg_1 = float(input("\nEnter first leg of the triangle: "))
leg_2 = float(input("\nEnter second leg of the triangle: "))


#Code program
hypotenuse = math.sqrt(leg_1**2 + leg_2**2)
hypotenuse = round(hypotenuse, 3)
squere = leg_1*leg_2*0.5
squere = round(squere, 3)


#Result
print("\nFor a triangle with legs of " + str(leg_1) + " and " + str(leg_2) + " the hypotenuse is " + str(hypotenuse))
print("\nFor a triangle with legs of " + str(leg_1) + " and " + str(leg_2) + " the squere is " + str(squere))
