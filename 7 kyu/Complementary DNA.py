def DNA_strand(dna):
    # Initialize an empty string to store the complementary strand
    complementary_strand = ""
    
    # Create a dictionary to define the complementary pairs
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Iterate through each character in the input DNA strand
    for char in dna:
        # Use the dictionary to find the complement and append it to the result
        complementary_strand += complements[char]
    
    return complementary_strand
