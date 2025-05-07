import random

class RobotDFS:
    def __init__(self, N, start, goal):
        self.N = N
        self.grid = [[0 for _ in range(N)] for _ in range(N)]  # 0 represents open space
        self.start = start
        self.goal = goal
        self.visited = set()
        self.path = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        # Place random obstacles (1 represents an obstacle)
        self.generate_obstacles()

    def generate_obstacles(self):
        num_obstacles = (self.N * self.N) // 4  # About 25% of the grid is obstacles
        obstacles = random.sample(range(self.N * self.N), num_obstacles)
        
        for idx in obstacles:
            x, y = divmod(idx, self.N)
            if (x, y) != self.start and (x, y) != self.goal:  # Ensure start and goal are not obstacles
                self.grid[x][y] = 1

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def is_valid(self, x, y):
        # Check if (x, y) is within bounds and is not an obstacle
        return 0 <= x < self.N and 0 <= y < self.N and self.grid[x][y] == 0

    def dfs(self, x, y):
        # If we reach the goal, return True
        if (x, y) == self.goal:
            self.path.append((x, y))
            return True
        
        # Mark the current node as visited
        self.visited.add((x, y))
        self.path.append((x, y))

        # Explore all 4 directions
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and (nx, ny) not in self.visited:
                if self.dfs(nx, ny):
                    return True

        # Backtrack if no valid path found
        self.path.pop()
        return False

    def find_path(self):
        # Start DFS from the start node
        if self.dfs(self.start[0], self.start[1]):
            return self.path
        else:
            return None

# Main Program
if __name__ == "__main__":
    # Input: Grid size N
    N = int(input("Enter the grid size N: "))

    # Input: Starting point (x, y)
    start_x = int(input(f"Enter the starting x-coordinate (0 to {N-1}): "))
    start_y = int(input(f"Enter the starting y-coordinate (0 to {N-1}): "))

    # Input: Goal point (x, y)
    goal_x = int(input(f"Enter the goal x-coordinate (0 to {N-1}): "))
    goal_y = int(input(f"Enter the goal y-coordinate (0 to {N-1}): "))

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    # Create RobotDFS object and generate the grid with obstacles
    robot = RobotDFS(N, start, goal)

    # Print the generated grid
    print("\nGenerated Grid (0 = Open, 1 = Obstacle):")
    robot.print_grid()

    # Find and print the path using DFS
    path = robot.find_path()

    if path:
        print("\nPath found (DFS traversal):")
        for step in path:
            print(step)
    else:
        print("\nNo path found from start to goal.")
