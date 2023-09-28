 def find_multiples(integer, limit):
    multiples = []
    
    # Iterate through numbers from integer up to limit
    for num in range(integer, limit + 1, integer):
        multiples.append(num)
    
    return multiples
