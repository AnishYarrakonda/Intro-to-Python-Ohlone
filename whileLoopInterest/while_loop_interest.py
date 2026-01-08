#Programmer: Anish Yarrakonda
#Lab 3: Interest Rate

from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\nName         : CNET-142 Lab 3 Interest Rate - Anish Yarrakonda")
print(f"Program      : print_me_first.py")
print(f"Current Time : {current_time}\n")

while True:
    p = float(input("Enter the starting principal, 0 to quit: "))
    if p <= 0:
        print("Program exiting .... ")
        break
    
    r = float(input("Enter the annual interest rate: "))
    n = float(input("How many times per year is the interest compounded? "))
    t = float(input("For how many years will the account earn interest? "))
    total = p * (1 + float(r/100) / n) ** (n*t)
    interest = total - p

    print(f"At the end of {t} years, you will have ${total:,.2f} with interest ${interest:,.2f} earned.\n")
    