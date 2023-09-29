def derive(coefficient, exponent):
    # Calculate the new coefficient and exponent
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    
    # Construct the string representation
    if new_exponent == 1:
        result = f"{new_coefficient}x"
    else:
        result = f"{new_coefficient}x^{new_exponent}"
    
    return result
