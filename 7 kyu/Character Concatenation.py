def char_concat(s):
    # Check if the string has an odd length and remove the central character if it does
    if len(s) % 2 == 1:
        s = s[:len(s) // 2] + s[(len(s) // 2) + 1:]
    
    result = ''
    
    # Concatenate the characters as described
    for i in range(len(s) // 2):
        result += s[i] + s[len(s) - 1 - i] + str(i + 1)
    
    return result
