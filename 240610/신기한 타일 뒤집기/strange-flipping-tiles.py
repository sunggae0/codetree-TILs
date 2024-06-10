def flip_tiles(n, commands):
    # Initialize the tile list. Assuming starting at index 0.
    # Let's use a dictionary to store tile colors dynamically.
    # True represents a white tile, False represents a black tile.
    tiles = {}
    current_position = 0

    for command in commands:
        x, direction = command.split()
        x = int(x)
        
        if direction == 'R':
            for i in range(x):
                pos = current_position + i
                tiles[pos] = False  # Flip to black
            current_position += x - 1  # Move to the last flipped position
        elif direction == 'L':
            for i in range(x):
                pos = current_position - i
                tiles[pos] = True  # Flip to white
            current_position -= x - 1  # Move to the last flipped position
    
    # Count white and black tiles
    white_count = sum(1 for color in tiles.values() if color)
    black_count = sum(1 for color in tiles.values() if not color)
    
    return white_count, black_count

# Input reading part
n = int(input().strip())
commands = [input().strip() for _ in range(n)]

# Process and get the result
white_count, black_count = flip_tiles(n, commands)

# Print the result
print(white_count, black_count)