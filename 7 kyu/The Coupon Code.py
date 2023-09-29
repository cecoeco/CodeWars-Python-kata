import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # Import the datetime module to work with dates
    
    # Define a function alias 'strptime' for datetime.datetime.strptime for brevity
    strptime = datetime.datetime.strptime
    
    # Define the expected date format
    date_format = "%B %d, %Y"
    
    # Parse the current date string into a datetime object
    current_datetime = strptime(current_date, date_format)
    
    # Parse the expiration date string into a datetime object
    expiration_datetime = strptime(expiration_date, date_format)
    
    # Check if the entered code matches the correct code using 'is' for identity
    is_code_correct = entered_code is correct_code
    
    # Check if the current date is less than or equal to the expiration date
    is_not_expired = current_datetime <= expiration_datetime
    
    # Determine if the coupon is valid based on the code and expiration date
    is_valid_coupon = is_code_correct and is_not_expired
    
    # Return True if the coupon is valid, False otherwise
    return is_valid_coupon
