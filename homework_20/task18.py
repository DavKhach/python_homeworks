def compound_interest(principal, rate, times_compounded, years):
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    number_of_payments = years * 12
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)

def investment_return(initial_investment, annual_rate, years):
    return initial_investment * (1 + annual_rate) ** years


financial_operations = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return
}


def financial_calculator(operation, **kwargs):
    if operation not in financial_operations:
        raise ValueError("Invalid operation")
    
    calculation_func = financial_operations[operation]
    
    return calculation_func(**kwargs)


print(financial_calculator('compound_interest', principal=1000, rate=0.05, times_compounded=4, years=10))
print(financial_calculator('loan_payment', principal=20000, annual_rate=0.05, years=5))
print(financial_calculator('investment_return', initial_investment=1000, annual_rate=0.07, years=10))
