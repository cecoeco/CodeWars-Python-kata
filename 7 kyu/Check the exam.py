def check_exam(arr1, arr2):
    # Initialize a variable to store the score
    score = 0
    
    # Iterate through the answers using a loop
    for i in range(len(arr1)):
        # Check if the student's answer is correct or blank
        if arr2[i] == arr1[i]:
            score += 4  # +4 for correct answer
        elif arr2[i] == "":
            score += 0  # +0 for blank answer
        else:
            score -= 1  # -1 for incorrect answer
    
    # Ensure the score is not negative
    if score < 0:
        score = 0
    
    return score
