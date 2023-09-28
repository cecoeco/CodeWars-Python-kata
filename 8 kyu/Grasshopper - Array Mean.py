def find_average(nums):
    # Check if the input list is empty to avoid division by zero
    if len(nums) == 0:
        return 0
    
    # Calculate the sum of the numbers in the list
    total = sum(nums)
    
    # Calculate the average by dividing the sum by the number of values
    average = total / len(nums)
    
    return average
