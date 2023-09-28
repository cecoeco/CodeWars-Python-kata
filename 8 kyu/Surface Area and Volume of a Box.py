def get_size(width, height, depth):
    # Calculate surface area
    surface_area = 2 * (width * height + height * depth + depth * width)
    
    # Calculate volume
    volume = width * height * depth
    
    # Return results as an array
    return [surface_area, volume]

