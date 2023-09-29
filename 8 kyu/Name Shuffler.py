def name_shuffler(str_):
    # Split the input string into words using whitespace as the delimiter
    words = str_.split()
    
    # Reverse the order of the words
    reversed_name = " ".join(reversed(words))
    
    return reversed_name
