def cube_checker(volume, side):
    # Check for invalid input (volume or side is less than or equal to 0)
    if volume <= 0 or side <= 0:
        return False
    
    # Calculate the expected volume of a cube with equal sides
    expected_volume = side ** 3
    
    # Compare the expected volume with the given volume
    return volume == expected_volume
