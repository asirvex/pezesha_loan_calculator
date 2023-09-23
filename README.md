# Loan Repayment Calculator

This Python script provides a loan repayment calculator that allows you to calculate the total interest, total amount to be repaid, and a detailed breakdown of loan repayments over a specified loan term. The calculator takes into account the loan amount, loan term (in months), annual interest rate, and repayment frequency (monthly, bi-monthly, or weekly).

## Getting Started

### Prerequisites

- Python 3.x
- No additional packages or dependencies are required.

### Usage

1. Clone the repository the Pezesha loan calculator using:  `git clone git@github.com:asirvex/pezesha_loan_calculator.git`
2. cd into the directory. `cd pezesha_loan_calculator`
3. Run the repayment calculator in the main file i.e `python main.py loan_amount loan_term_months annual_interest_rate repayment_frequency`

   **Example**

```python
python main.py loan_amount loan_term_months annual_interest_rate repayment_frequency
**Arguments:**

* `loan_amount`: The amount of the loan.
* `loan_term_months`: The length of the loan in months.
* `annual_interest_rate`: The annual interest rate of the loan.
* `repayment_frequency`: The repayment frequency of the loan, either `monthly`, `bi-monthly`, or `weekly`.

**Example:**

python
python main.py 10000 36 5 monthly
```

**Output:**

```
Payment Number | Monthly Payment | Principal Payment | Interest Payment | Remaining Balance
------------- | -------------- | ----------------- | ---------------- | ----------------
1              | 285.22             | 278.33              | 6.89          | 9721.67
2              | 285.22             | 278.64              | 6.58          | 9443.03
3              | 285.22             | 278.96              | 6.26          | 9164.07
...
36             | 285.22             | 285.22              | 0.00          | 0.00
```

```
Total Interest Paid: $265.19
Total Amount to be Repaid: $10265.19
```
