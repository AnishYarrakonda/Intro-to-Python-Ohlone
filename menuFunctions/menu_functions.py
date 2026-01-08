# Programmer: Anish Yarrakonda
# Date: 7/11/2025
# menu_functions.py

from printMeFirst import print_me_first
import simple_interest
import mortgage

if __name__ == "__main__":
    print_me_first.print_me_first(
        lab_info = "CNET-142 Lab 4 Menu Functions - Anish Yarrakonda",
        program_name="menu_functions.py"
        )

    while True:
        menu_selection = int(input("""
-------------------------------
1   Calculate Simple Interest
2   Calculate Mortgage Payment
99  Quit the program                                
-------------------------------
                                   
Select one of the command numbers above: """))
        
        if menu_selection == 99:
            print("\nHave a nice day...")
            break
        elif menu_selection == 1:
            print("\nCalculating Simple Interest\n")
            simple_interest.simple_interest()
        elif menu_selection == 2:
            print("\nCalculating Mortgage\n")
            mortgage.mortgage()
        else:
            print("\nError: command not recognized")