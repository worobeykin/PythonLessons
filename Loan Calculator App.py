#Loan Calculator App
import matplotlib.pyplot as plt

def loan_info():
    """Get user info about loan"""
    loan = {}
    loan_amount = float(input("\nEnter the loan amount: "))
    loan['Principal'] = loan_amount
    interest_rate = float(input("Enter the interest rate: "))
    loan['Rate'] = interest_rate / 100
    monthly_payment = float(input("Enter the monthly payment: "))
    loan['Monthly Payment'] = monthly_payment
    loan['Money Paid'] = 0
    return loan
    
def show_loan_info(loan, nomber_of_months):
    """Show current info about loan"""
    print("\n----Loan information after " + str(nomber_of_months) + " months----")
    for key, value in loan.items():
        print(key + ": " + str(value))
        
def collect_interest(loan):
    """Update current loan"""
    loan['Principal'] = loan['Principal'] + loan['Principal'] * loan['Rate'] / 12    
    
def make_monthly_payment(loan):
    """Determining the payment balance"""
    loan['Principal'] = loan['Principal'] - loan['Monthly Payment']
    if loan['Principal'] > 0:
        loan['Money Paid'] += loan['Monthly Payment']
    else:
        loan['Money Paid'] += loan['Monthly Payment'] + loan['Principal']
        loan['Principal'] = 0

def summarize_loan(loan, nomber_of_months, initial_principle):
    """Summary result"""
    print("It took you " + str(nomber_of_months) + " months to make the payment")
    print("\nYour initial loan was $" + str(initial_principle) + " at a rate of " + str(loan['Rate']*100) + "%")
    print("Your monthly payment was $" + str(loan['Monthly Payment']))
    print("You spent $" + str(loan['Money Paid']) + " total")
    print("You spent $" + str(loan['Money Paid'] - initial_principle) + " on interest")

def create_graph(data, loan):
    """Visual loan"""
    x_values = []
    y_values = []
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])
    plt.plot(x_values, y_values)
    plt.title(str(100*loan['Rate']) + "% Interest" + " With $" + str(loan['Monthly Payment']) + " Monthly Payment")
    plt.xlabel("Month Number")
    plt.ylabel("Principal of Loan")
    plt.show()

#Main code

print("Welcome to the Loan Calculator App")

nomber_of_months = 0
my_loan = loan_info()
starting_principle = my_loan['Principal']
data_to_plot = []


show_loan_info(my_loan, nomber_of_months)
input("Press 'enter' to begin paying off your loan")

while my_loan['Principal'] > 0:
    if my_loan['Principal'] > starting_principle:
        print("\nYou will never pay off the loan")
        break
    nomber_of_months += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((nomber_of_months, my_loan['Principal']))
    show_loan_info(my_loan, nomber_of_months)
    if my_loan['Principal'] <= 0:
        summarize_loan(my_loan, nomber_of_months, starting_principle)
        create_graph(data_to_plot, my_loan)

    else:
        print("\nYou will NEVER pay off your loan!!!")
        print("You cannot get ahead of the interest! :-(")
        
            
        
        
















