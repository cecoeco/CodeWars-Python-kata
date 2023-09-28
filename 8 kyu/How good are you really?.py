def better_than_average(class_points, your_points):
    # Calculate the average of your peers' scores
    average_class_score = sum(class_points) / len(class_points)
    
    # Compare your score with the average
    return your_points > average_class_score
