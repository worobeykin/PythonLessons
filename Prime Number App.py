#Prime Number App
import time

print("Welcome to the Prime Number App")

flag = True

# While loop
while flag:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = int(input("Enter your choice: "))

    #Mode selection
    if choice == 1:
        given_number = int(input("What is your number: "))
        prime_status = True
        for i in range(2, given_number):
            if given_number % i == 0:
                prime_status = False
                break
        if prime_status == True:
            print("\n" + str(given_number) + " is prime!")
        else:
            print("\n" + str(given_number) + " is not prime!")
        
    elif choice == 2:
        start = int(input("Input star number of range: "))
        finish = int(input("Input finish number of range: "))
        secuence = []       
        start_time = time.time()

        for i in range(start, finish+1):
            prime_status = True
            if i > 1:
                for num in range(2, i):
                    if i % num == 0:
                        prime_status = False
                        break
            else:
                prime_status = False

            if prime_status == True:
                secuence.append(i)
        end_time = time.time()
        delta_time = end_time - start_time
        
        print("\nCalculation took a total of " + str(round(delta_time, 4)) + " seconds")
        input("Press enter to continue.")
        print("The following numbers between " + str(start) + " and " + str(finish) + " are prime:")
        for i in secuence:
            print(i)
    else:
        print("\nThat is not valid option")

    #Question about escape the program
    the_end = input("\nWould you like to run the program again (y/n): ").strip().lower()
    if the_end == 'y':
        continue
    elif the_end == 'n':
        print("\nGoodbay")
        flag = False
    else:
        print("\nYou input invalid option! Goodbay")
        flag = False
        
        
        
        
    







        
