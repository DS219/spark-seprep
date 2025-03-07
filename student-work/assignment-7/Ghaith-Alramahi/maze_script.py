import random

def generate_maze(width, height):
    maze = ""
    for _ in range(height):
        maze += "".join(random.choice("# ") for _ in range(width)) + "\n"
    return maze

# Generate and print a 20x10 random maze
maze_output = generate_maze(20, 10)
print(maze_output)
