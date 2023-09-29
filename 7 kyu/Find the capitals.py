def capitals(word):
    # Initialize an empty list to store the indexes of capital letters
    capital_indexes = []
    
    # Use list comprehension to iterate through characters and their indexes
    for index, char in enumerate(word):
        # Check if the character at the current index is an uppercase letter
        if char.isupper():
            # If it's uppercase, add its index to the capital_indexes list
            capital_indexes.append(index)
    
    # Return the list containing the indexes of capital letters
    return capital_indexes
