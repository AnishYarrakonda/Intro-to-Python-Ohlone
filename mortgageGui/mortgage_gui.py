# mortgage_gui.py

import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt
from print_me_first import print_me_first
from mortgage import calculate_mortgage


# function name: on_calculate
# function description: Handles the "Calculate" button press. It validates user inputs and calculates the monthly mortgage payment and total paid.
# @param loan_entry: An Entry widget for the loan amount.
# @param rate_entry: An Entry widget for the interest rate.
# @param term_entry: An Entry widget for the loan term in years.
# @param monthly_payment_var: A StringVar to display the monthly payment.
# @param total_paid_var: A StringVar to display the total paid.
# @return: None
def on_calculate(loan_entry, rate_entry, term_entry, monthly_payment_var, total_paid_var):
    try:
        loan_amount = float(loan_entry.get())
        interest_rate = float(rate_entry.get())
        loan_term_years = float(term_entry.get())

        if loan_amount <= 0 or interest_rate < 0 or loan_term_years <= 0:
            messagebox.showerror("Invalid Input", "All values must be positive numbers.")
            return

        monthly, total = calculate_mortgage(loan_amount, interest_rate, loan_term_years)

        monthly_payment_var.set(f"${monthly:,.2f}")
        total_paid_var.set(f"${total:,.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for all fields.")

# function name: on_chart
# function description: Handles the "Chart" button press. It reads mortgage data from a csv file and plots a line chart.
# @param: None
# @return: None
def on_chart():
    try:
        years = []
        rates = []
        with open("/Users/anish/Documents/Python Coding Practice/Intro_to_Python_Course_@Ohlone/mortgageGui/mortgageRate.txt", 'r') as file:
            # Skip the header row
            next(file)
            for line in file:
                line = line.strip()
                if line:
                    year, rate = line.split(',')
                    years.append(int(year))
                    rates.append(float(rate))

        # Plotting the line chart
        plt.figure(figsize=(10, 6))
        plt.plot(years, rates, marker='o', linestyle='-')
        plt.title('Historical 30-Year Fixed Mortgage Rates')
        plt.xlabel('Year')
        plt.ylabel('Interest Rate (%)')

        # Add labels to the data points
        for x, y in zip(years, rates):
            plt.text(x, y, f'{y:.2f}%', ha='center', va='bottom')

        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The 'mortgageRate.txt' file was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while plotting the chart: {e}")

# function name: setup_gui
# function description: Sets up the main GUI window and its widgets for the mortgage calculator application.
# @param: None
# @return: None
def setup_gui():
    root = tk.Tk()
    root.title("Mortgage Calculator")
    root.configure(bg="light blue")
    root.geometry("1200x600")

    # configure the grid
    for i in range(6):
        root.rowconfigure(i, weight=1)
    for i in range(3):
        root.columnconfigure(i, weight=1)

    # input fields
    tk.Label(root, text="Loan Amount:", bg="light blue").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    loan_entry = tk.Entry(root)
    loan_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    tk.Label(root, text="Interest Rate %:", bg="light blue").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    rate_entry = tk.Entry(root)
    rate_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    tk.Label(root, text="Loan Term (Years):", bg="light blue").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    term_entry = tk.Entry(root)
    term_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    # output fields (Read ONLY)
    tk.Label(root, text="Monthly Payment:", bg="light blue").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    monthly_payment_var = tk.StringVar()
    monthly_payment_entry = tk.Entry(root, textvariable=monthly_payment_var, state="readonly", font=("Arial", 14, "bold", "italic"))
    monthly_payment_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    tk.Label(root, text="Total Paid:", bg="light blue").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    total_paid_var = tk.StringVar()
    total_paid_entry = tk.Entry(root, textvariable=total_paid_var, state="readonly", font=("Arial", 14, "bold", "italic"))
    total_paid_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    # buttons
    calculate_button = tk.Button(root, text="Calculate", command=lambda: on_calculate(loan_entry, rate_entry, term_entry, monthly_payment_var, total_paid_var), bg="light blue")
    calculate_button.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

    chart_button = tk.Button(root, text="Chart", command=on_chart)
    chart_button.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)

    # print_me_first textbox
    print_me_first_box = tk.Text(root, height=4, width=50, state="disabled")
    print_me_first_box.grid(row=0, column=2, rowspan=5, sticky="nsew", padx=50, pady=5)
    
    # insert the print_me_first info into the text box
    info = print_me_first("CNET-142 Lab 8 Mortgage GUI - Anish Yarrakonda", "lab8.py")
    print_me_first_box.config(state="normal")
    print_me_first_box.delete("1.0", tk.END)
    print_me_first_box.insert(tk.END, info)
    print_me_first_box.config(state="disabled")

    root.mainloop()

# main program
if __name__ == "__main__":
    setup_gui()