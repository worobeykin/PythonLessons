#Average Calculator App

print("Welcome to the Average Calculator App")

#Ask user
name = input("What is your name: ").title()
amount_grades = int(input("How many grades would you like to enter: "))
grades = []
sum_grades = 0

for i in range(amount_grades):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("\nGrades Highest to Lowest:")
sort_grades = sorted(grades, reverse=True)
print("\t" + "\n\t".join(map(str,sort_grades)))

#Display info
print(name + "'s Grade Summary:")
print("\tTotal number of grades: " + str(amount_grades))
print("\tHighest grade: " + str(sort_grades[0]))
print("\tLowest grade: " + str(min(grades)))
print("\tAverage grade: " + str(round(sum(grades)/amount_grades, 2)))

#Desire average
desire_average = float(input("\nWhat is your desired average: "))
print("Good like " + name + "!")
add_grade = desire_average * (amount_grades+1) - sum(grades)
print("You will need to get a " + str(round(add_grade, 2)) + " on your next assignment to earn a " + str(desire_average) + " average")


#Replase
print("\nImangine new grades")
chage_grade = int(input("What grade would you like to change:"))
new_grade = int(input("What grade would you like to change " + str(chage_grade) + " to:"))
imagine_grades = grades.copy()
imagine_grades.remove(chage_grade)
imagine_grades.append(new_grade)

print("\nNew Grades Highest to Lowest:")
sort_grades = sorted(imagine_grades, reverse=True)
print("\t" + "\n\t".join(map(str,sort_grades)))

#Display info
print(name + "'s Grade Summary:")
print("\tTotal number of grades: " + str(amount_grades))
print("\tHighest grade: " + str(sort_grades[0]))
print("\tLowest grade: " + str(min(imagine_grades)))
print("\tAverage grade: " + str(round(sum(imagine_grades)/amount_grades, 2)))
new_number = sum(imagine_grades)/amount_grades
last_number = sum(grades)/amount_grades
point = round((new_number - last_number), 2)
print("\nYour new average is " + str(round(sum(imagine_grades)/amount_grades, 2)) + "your last average is: " + str(round(sum(grades)/amount_grades, 2)))
print("Difrent is: " + str(point))

print("\nOriginal: " + str(grades))
