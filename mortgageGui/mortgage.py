# mortgage.py
# same as mortgage lab
# returns monthly payment and total payment instead of printing it to terminal

def calculate_mortgage(loan_amount, interest_rate, loan_term_years):
    monthly_rate = (interest_rate / 100) / 12
    num_payments = loan_term_years * 12

    if monthly_rate == 0:
        monthly_payment = loan_amount / num_payments
    else:
        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    
    total_payment = monthly_payment * num_payments
    return monthly_payment, total_payment