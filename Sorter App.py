#Sorter App

print("Welcome to the Grade Sorter App")

grades = []

#Ask users
grades.append(input("\nWhat is your firs grade: "))
grades.append(input("What is your second grade: "))
grades.append(input("What is your thrid grade: "))
grades.append(input("What is your fourth grade: "))

print("\nYour grades are:" + str(grades))

sort_grades = sorted(grades, reverse=True)
print("\nYour grades from highest to lowest are: " + str(sort_grades))

print(grades)

grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades))

print("\nThe lowest two grades will naw be dropped.")

#Remove grades
remove_1 = sort_grades.pop(3)
remove_2 = sort_grades.pop(2)
print("Removed grade: " + str(remove_1))
print("Removed grade: " + str(remove_2))

print("\nYour remaining grades are: " + str(sort_grades))


print("\nNice work! Your highest grade is a " + str(sort_grades[0]))


