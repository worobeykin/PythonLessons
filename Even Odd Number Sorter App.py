#Even Odd Number Sorter App

print("Welcome to the Even Odd Number Sorter App")

flag = True


while flag:
    results = []
    numbers = input("\nEnter numbers separated by a comma (,): ").strip()
    numbers = numbers.replace(" ", "")
    list_of_numders = numbers.split(",")
    results = [int(i) for i in list_of_numders]

    print(list_of_numders)
    print(results)
    
    evens = []
    odds = []
    print("\n---- Result Summary ----")
    for i in results:
        if i % 2 == 0:
            print(str(i) + " is even!")
            evens.append(i)
        else:
            print(str(i) + " is odd!")
            odds.append(i)
    
    evens = sorted(evens)
    print("\nThe following " + str(len(evens)) + " numbers are even:")
    print("\t" + "\n\t".join(str(i) for i in evens))

    odds.sort()
    print("\nThe following " + str(len(odds)) + " numbers are even:")
    print("\t" + "\n\t".join(str(i) for i in odds))
            
    
    choice = input("\nRun again (y/n): ")
    if choice != 'y':
        print("Goodbay")
        flag = False
    
        
         
