import re

def reverse_words(text):
    # Use regular expressions to split the input text into words
    words = re.findall(r'\S+|\s+', text)
    
    # Initialize an empty list to store the reversed words
    reversed_words = []
    
    # Iterate through each word and reverse it
    for word in words:
        # Reverse the word if it's not a space
        if word != ' ':
            reversed_word = word[::-1]
        else:
            reversed_word = word
        
        # Add the reversed word to the list of reversed words
        reversed_words.append(reversed_word)
    
    # Join the reversed words to reconstruct the text
    reversed_text = ''.join(reversed_words)
    
    return reversed_text
