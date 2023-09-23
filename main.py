def calculate_monthly_payment(loan_amount, annual_interest_rate, num_payments):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / \
                      ((1 + monthly_interest_rate) ** num_payments - 1)
    return monthly_payment

def generate_repayment_schedule(loan_amount, num_payments, monthly_payment, annual_interest_rate):
    remaining_balance = loan_amount
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    repayment_schedule = []

    for payment_num in range(1, num_payments + 1):
        monthly_interest = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - monthly_interest
        remaining_balance -= principal_payment

        repayment_schedule.append({
            'Payment Number': payment_num,
            'Monthly Payment': round(monthly_payment, 2),
            'Principal Payment': round(principal_payment, 2),
            'Interest Payment': round(monthly_interest, 2),
            'Remaining Balance': round(remaining_balance, 2)
        })

    return repayment_schedule

def loan_repayment_calculator(loan_amount, loan_term_months, annual_interest_rate, repayment_frequency):
    MONTHS_PER_YEAR = 12
    WEEKS_PER_YEAR = 52

    if repayment_frequency == 'monthly':
        num_payments = loan_term_months
    elif repayment_frequency == 'bi-monthly':
        num_payments = loan_term_months // 2
    elif repayment_frequency == 'weekly':
        num_payments = loan_term_months * MONTHS_PER_YEAR // WEEKS_PER_YEAR
    else:
        raise ValueError("Invalid repayment frequency")

    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, num_payments)
    repayment_schedule = generate_repayment_schedule(loan_amount, num_payments, monthly_payment, annual_interest_rate)
    total_interest_paid = sum(payment['Interest Payment'] for payment in repayment_schedule)
    total_amount_repaid = loan_amount + total_interest_paid

    results = {
        'Total Interest Paid': round(total_interest_paid, 2),
        'Total Amount to be Repaid': round(total_amount_repaid, 2),
        'Repayment Schedule': repayment_schedule
    }

    return results

# Example usage:
loan_amount = 10000
loan_term_months = 36
annual_interest_rate = 5.0  # 5% annual interest rate
repayment_frequency = 'monthly'

result = loan_repayment_calculator(loan_amount, loan_term_months, annual_interest_rate, repayment_frequency)

for row in result['Repayment Schedule']:
    print(row)
print(f"Total Interest Paid: ${result['Total Interest Paid']}")
print(f"Total Amount to be Repaid: ${result['Total Amount to be Repaid']}")
