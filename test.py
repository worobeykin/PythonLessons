print("Welcome to the Grade Sorter App")

#Initialize list and get user input
grades = []
grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)

print("\nYour grades are: " + str(grades))
