# simple_interest.py

"""
Function name: simple_interest
Function description: Calculates and displays interest details (total amount earned, total interest earned, after t years) based on user input.
                      Allows the user to exit the calculation loop by entering 0 for loan amount.
@param: No direct parameters. Obtains input from the user through console.
@return: None. Prints the calculated mortgage details to the console.
"""

def simple_interest():
    while True:
        p = float(input("Enter the starting principal, 0 to quit: "))
        if p <= 0:
            print("\nExiting Simple Interest program .... \n")
            break
        
        r = float(input("Enter the annual interest rate: "))
        n = float(input("How many times per year is the interest compounded? "))
        t = float(input("For how many years will the account earn interest? "))
        total = p * (1 + float(r/100) / n) ** (n*t)
        interest = total - p

        print(f"At the end of {t} years, you will have ${total:,.2f} with interest ${interest:,.2f} earned.\n")