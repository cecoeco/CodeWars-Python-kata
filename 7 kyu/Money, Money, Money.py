def calculate_years(principal, interest, tax, desired):
    # Initialize the number of years
    years = 0
    
    # Keep calculating until the principal reaches or exceeds the desired amount
    while principal < desired:
        # Calculate interest accrued for the year
        interest_accrued = principal * interest
        
        # Calculate tax on the interest accrued
        tax_paid = interest_accrued * tax
        
        # Update the principal after tax is paid
        principal += interest_accrued - tax_paid
        
        # Increment the number of years
        years += 1
    
