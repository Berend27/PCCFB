# Kapitel 2 - Loops & Conditionals
# Loop Leviathan - checks a list of tasks to determine whether
# a maze gets solved

# Define the list of tasks representing the maze
tasks = ["move forward", "move forward", "turn left", "move forward", "write Python code", "turn right", "move forward"]

# Initialize variables to keep track of position and direction
position = 0
direction = "north"
 # Start navigating through the maze
for task in tasks:
    if task == "move forward":
        position += 1
        print(f"Moved forward to position {position} while facing {direction}.")
    elif task == "turn left":
        if direction == "north":
            direction = "west"
        elif direction == "west":
            direction = "south"
        elif direction == "south":
            direction = "east"
        elif direction == "east":
            direction = "north"
        print(f"Turned left, now facing {direction}.")
    elif task == "turn right":
        if direction == "north":
            direction = "east"
        elif direction == "east":
            direction = "south"
        elif direction == "south":
            direction = "west"
        elif direction == "west":
            direction = "north"
        print(f"Turned right, now facing {direction}.")
    elif task == "obstacle":
        print(f"Encountered an obstacle at position {position}, cannot proceed.")
        break
    else:
        print(f"Unknown task '{task}' encountered.")
 # Check if the maze was completed
if task != "obstacle":
    print(f"Congratulations! You have successfully navigated through the maze and defeated the Loop Leviathan!")
else:
    print("Leider haben Sie nicht abgeschlossen.")
