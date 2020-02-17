#DataBase Admin Program

print("Welcome to the Database program App.")

log_on_information = {
    "Sany":'123456qw',
    "Sany2":'123456wq',
    "alex":'1qaz2wsx',
    "admin00":'Qwerty123',
    }

username = input("What is your name: ")

if username in log_on_information.keys():
    passwd = input("What is your password: ")
    if passwd in log_on_information[username]:
        print("\nHello " + username + ". You are logged in!\n")
        if username == 'admin00':
            print("Whole database:")
            for key, value in log_on_information.items():
                print("Username: " + key + "\t\t" " Password: " + value)
        else:
            agree = input("Do you want to change the password(yes/no): ")
            if agree == 'yes':
                new_passwd = input("The password should have 8 characters: ")
                if len(new_passwd) < 8:
                    print("New password is not enough characters")
                else:
                    log_on_information[username] = new_passwd
                    print("\n" + username + " your password is " + str(log_on_information[username]))
            else:
                print("\nGoodbay")
    else:
        print("Access denied")
else:
    print(username + " is not the database")
                
                
