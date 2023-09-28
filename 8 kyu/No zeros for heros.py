def no_boring_zeros(n):
    # Convert the number to a string
    num_str = str(n)

    # Remove trailing zeros
    while num_str.endswith('0'):
        num_str = num_str[:-1]

    # Check if the result is an empty string (all zeros)
    if num_str == '':
        return 0
    
    # Convert the result back to an integer if it's an integer
    return int(num_str)
