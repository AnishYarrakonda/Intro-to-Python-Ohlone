# mortgage.py

"""
Function name: mortgage
Function description: Calculates and displays mortgage payment details (monthly payment, total paid, total interest) based on user input.
                      Allows the user to exit the calculation loop by entering 0 for loan amount.
@param: No direct parameters. Obtains input from the user through console.
@return: None. Prints the calculated mortgage details to the console.
"""

def mortgage():
    print("\n--- Mortgage Payment Calculator ---")
    while True:
        loan_amount = float(input("Enter the loan amount (0 to quit): "))
        if loan_amount <= 0:
            print("\nExiting Mortgage program .... \n")
            break # Exit the loop if user enters 0 or less

        interest_rate = float(input("Enter the annual loan interest rate (%): "))
        loan_term_years = float(input("Enter the loan term (number of years): "))

        monthly_rate = (interest_rate / 100) / 12
        num_payments = loan_term_years * 12

        monthly_payment = loan_amount * monthly_rate * pow((1 + monthly_rate), num_payments) / (pow((1 + monthly_rate), num_payments) - 1)

        total_payment = monthly_payment * num_payments
        interest_paid = total_payment - loan_amount

        print(f"\nFor a loan of ${loan_amount:,.2f} at {interest_rate:.2f}% for {int(loan_term_years)} years:")
        print(f"Monthly Payment: ${monthly_payment:,.2f}")
        print(f"Total Paid:      ${total_payment:,.2f}")
        print(f"Total Interest:  ${interest_paid:,.2f}")
        print("") # blank line for readability