def sum_digits(number):
    # Take the absolute value of the input number
    number = abs(number)
    
    # Convert the number to a string to iterate through its digits
    number_str = str(number)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0
    
    # Iterate through the digits and add their absolute values to the sum
    for digit in number_str:
        digit_sum += int(digit)
    
    return digit_sum
