#Programmer: Anish Yarrakonda

#Lab1 Header Code
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\nName         : CNET-142 Lab 2 Tax Rate - Anish Yarrakonda")
print(f"Program      : taxrate.py")
print(f"Current Time : {current_time}\n")

# Constants for tax rates
RATE1 = 0.10
RATE2 = 0.12
RATE3 = 0.22
RATE4 = 0.24
RATE5 = 0.32
RATE6 = 0.35
RATE7 = 0.37

# Constants for single filer tax brackets
RATE1_SINGLE_LIMIT = 11600
RATE2_SINGLE_LIMIT = 47150
RATE3_SINGLE_LIMIT = 100525
RATE4_SINGLE_LIMIT = 191950
RATE5_SINGLE_LIMIT = 243725
RATE6_SINGLE_LIMIT = 609350

# Constants for married filer tax brackets
RATE1_MARRIED_LIMIT = 23200
RATE2_MARRIED_LIMIT = 94300
RATE3_MARRIED_LIMIT = 201050
RATE4_MARRIED_LIMIT = 383900
RATE5_MARRIED_LIMIT = 487450
RATE6_MARRIED_LIMIT = 731200

# Get user input
income = float(input("Please enter your income: "))
status = input("Please enter s for single, m for married: ").lower()

# Determine tax bracket limits
if status == 's':
    limits = [
        RATE1_SINGLE_LIMIT,
        RATE2_SINGLE_LIMIT,
        RATE3_SINGLE_LIMIT,
        RATE4_SINGLE_LIMIT,
        RATE5_SINGLE_LIMIT,
        RATE6_SINGLE_LIMIT
    ]
elif status == 'm':
    limits = [
        RATE1_MARRIED_LIMIT,
        RATE2_MARRIED_LIMIT,
        RATE3_MARRIED_LIMIT,
        RATE4_MARRIED_LIMIT,
        RATE5_MARRIED_LIMIT,
        RATE6_MARRIED_LIMIT
    ]
#If the user incorrectly entered the marital status, the program will terminate.
else:
    print("Invalid status entered.")
    exit()

# Brackets and variables
brackets = [RATE1, RATE2, RATE3, RATE4, RATE5, RATE6, RATE7]        # Define all tax rates in a list
prev_Limit = 0                                                      # Initialize the lower bound of the current tax bracket
taxes = []                                                          # Create an empty list to store tax calculated for each bracket

# Tax calculation
for i in range(6):                                  # Loop through the first six tax brackets (0 to 5)
    if income > limits[i]:                          # Check if income exceeds the current bracket's upper limit
        amount = limits[i] - prev_Limit             # Calculate the taxable amount within this specific bracket
        taxes.append(amount * brackets[i])          # Calculate tax for this segment and add to the list
        prev_Limit = limits[i]                      # Update the lower bound for the next bracket
    else:                                           # If income is less than or equal to the current bracket's limit
        amount = income - prev_Limit                # Calculate the remaining income that falls into this bracket
        if amount > 0:                              # Check if there's a positive amount left to tax in this bracket
            taxes.append(amount * brackets[i])      # Calculate and add tax for this final portion
        else:                                       # If no positive income left (already fully taxed)
            taxes.append(0)                         # Add zero tax for this bracket
        for j in range(i+1, 7):                     # Loop through all remaining higher tax brackets
            taxes.append(0)                         # Add zero tax for each of these unreached brackets
        break                                       # Exit the loop because the total income has been fully accounted for
else:                                               # This else runs only if the for loop completed all its iterations without breaking
    amount = income - limits[5]                     # Calculate the income portion falling into the highest (7th) bracket for large incomes 
    taxes.append(amount * brackets[6])              # Calculate and add tax for this highest bracket

# Unpack and sum taxes
tax1, tax2, tax3, tax4, tax5, tax6, tax7 = taxes    #Unpacks the values in the list taxes onto the variables tax1, tax2, ...
total_tax = sum(taxes)                              #Adds up the values in taxes

# Output Tax
print(f"The tax1 (10%) is ${tax1:,.2f}")
print(f"The tax2 (12%) is ${tax2:,.2f}")
print(f"The tax3 (22%) is ${tax3:,.2f}")
print(f"The tax4 (24%) is ${tax4:,.2f}")
print(f"The tax5 (32%) is ${tax5:,.2f}")
print(f"The tax6 (35%) is ${tax6:,.2f}")
print(f"The tax7 (37%) is ${tax7:,.2f}")
print()
print(f"Taxable income: ${income:,.2f}; Marital Status: {status}")
print(f"The tax is ${total_tax:,.2f}\n")