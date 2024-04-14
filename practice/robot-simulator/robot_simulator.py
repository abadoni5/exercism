# Approach:
# 1. Define the global constants NORTH, EAST, SOUTH, WEST to represent directions.
# 2. Implement the Robot class with attributes direction and coordinates representing its orientation and position.
# 3. Implement the move method to handle the movement instructions for the robot:
#     - For each movement instruction in the input string:
#         - If it's "R" (right turn), update the direction of the robot accordingly.
#         - If it's "L" (left turn), update the direction of the robot accordingly.
#         - If it's "A" (advance), update the coordinates of the robot based on its current direction.
# 4. Use index manipulation to handle the rotation of the robot to the right or left.
# 5. Update the coordinates of the robot when advancing based on its current direction.

# Globals for the directions
# Change the values as you see fit
NORTH = [0, 1]
EAST = [1, 0]
SOUTH = [0, -1]
WEST = [-1, 0]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        # Initialize the robot with direction and coordinates
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, mvr):
        # Define directions and iterate through movement instructions
        dir = [NORTH, EAST, SOUTH, WEST]
        for mv in mvr:
            # Update direction for 'R' (right turn) and 'L' (left turn)
            if mv == "R":
                if dir.index(self.direction) == 3:
                    self.direction = dir[0]
                else:
                    self.direction = dir[dir.index(self.direction) + 1]
            elif mv == "L":
                if dir.index(self.direction) == 0:
                    self.direction = dir[3]
                else:
                    self.direction = dir[dir.index(self.direction) - 1]
            # Update coordinates for 'A' (advance)
            elif mv == "A":
                self.coordinates = (self.coordinates[0] + self.direction[0],
                                    self.coordinates[1] + self.direction[1])
