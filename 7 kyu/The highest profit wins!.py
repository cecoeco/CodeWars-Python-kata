def min_max(lst):
    # Check if the input list is empty
    if not lst:
        return []

    # Initialize variables for minimum and maximum
    minimum = maximum = lst[0]

    # Iterate through the list to find the minimum and maximum
    for num in lst:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return [minimum, maximum]
