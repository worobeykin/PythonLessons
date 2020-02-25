#Bank Deposit and Withdrawal App

def get_info():
    """Get user information to store in a dict that represents a bank account"""
    print("Welcome to the Bank Deposit and Withdrawal App")
    name = input("Please enter your name: ").title().strip()
    savings = int(input("\nHow mach maney would you like to set up your savings account with: "))
    checking = int(input("How mach maney would you like to set up your checking account with: "))
    bank_account = {
        'Name': name,
        'Savings': savings,
        'Checking': checking,      
        }
    return bank_account

def make_deposit(bank_account, account, money):
    """Add money to a specific type of account"""
    bank_account[account] += money
    print("\nDeposited $" + str(money) + " into " + bank_account['Name'] + "'s " + account.lower() + " account")
    
def make_withdrawal(bank_account, account, money):
    """Withdrawal money to a specific type of account"""
    if bank_account[account] - money >= 0:
        bank_account[account] -= money
        print("\nWithdrew $" + str(money) + " from " + bank_account['Name'] + "'s " + account.lower() + " account")
    else:
        print("\nSorry, by withdrawing $" + str(money) + " you will have a negative balance")

def display_info(bank_account):
    """Display all information from dictionary"""
    print("\nCurrent Account Information")
    for key, value in bank_account.items():
        print(key + ": " + str(value))

#Main code
account = get_info()

flag = True
while flag:
    display_info(account)
    account_choice = input("\nWhat account would you like to access (Savings or Checking): ").title().strip()
    transaction_choice = input("What type of transaction would you like to make (Deposit or Withdrawal): ").title().strip()
    amount_money = float(input("How mach money: "))

    if account_choice == 'Savings' or account_choice == 'Checking':
        if transaction_choice == 'Deposit':
            make_deposit(account, account_choice, amount_money)          
        elif transaction_choice == 'Withdrawal':        
            make_withdrawal(account, account_choice, amount_money)
        else:
            print("The transaction cannot be completed")
    else:
            print("The transaction cannot be completed")

    end = input("\nWhould you like to make another transaction(y/n): ").lower().strip()
    if end != 'y':
        display_info(account)        
        flag = False
        print("\nThank you. Have a great day!")


    








        
    
















        
    
