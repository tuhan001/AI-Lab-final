class DFSPathFinder:
    def __init__(self, N, grid, start, destination):
        self.N = N
        self.grid = grid  # 2D grid representing the area
        self.start = start  # (x, y) coordinates of the source
        self.destination = destination  # (x, y) coordinates of the destination
        self.visited = set()  # To keep track of visited cells
        self.path = []  # List to store the path from source to destination
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid(self, x, y):
        # Check if (x, y) is within bounds and is not an obstacle (grid value should be 0)
        return 0 <= x < self.N and 0 <= y < self.N and self.grid[x][y] == 0

    def dfs(self, x, y):
        # If we reached the destination, return True
        if (x, y) == self.destination:
            self.path.append((x, y))
            return True

        # Mark the current cell as visited
        self.visited.add((x, y))

        # Explore all 4 possible directions (Right, Left, Down, Up)
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and (nx, ny) not in self.visited:
                if self.dfs(nx, ny):  # Recur for the next cell
                    self.path.append((x, y))
                    return True
        
        # Backtrack if no valid path is found
        return False

    def find_path(self):
        # Start DFS from the source
        if self.dfs(self.start[0], self.start[1]):
            self.path.reverse()  # Reverse the path to get the correct order
            return self.path
        else:
            return None

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))


# Main program
if __name__ == "__main__":
    # Input grid size N
    N = int(input("Enter the grid size N: "))

    # Create an empty grid (0 = open space, 1 = obstacle)
    grid = []
    print("Enter the grid row by row (0 for open space, 1 for obstacle):")
    for i in range(N):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        grid.append(row)

    # Input start and destination coordinates
    start_x = int(input(f"Enter the starting x-coordinate (0 to {N-1}): "))
    start_y = int(input(f"Enter the starting y-coordinate (0 to {N-1}): "))
    destination_x = int(input(f"Enter the destination x-coordinate (0 to {N-1}): "))
    destination_y = int(input(f"Enter the destination y-coordinate (0 to {N-1}): "))

    start = (start_x, start_y)
    destination = (destination_x, destination_y)

    # Create DFSPathFinder object
    dfs_finder = DFSPathFinder(N, grid, start, destination)

    # Print the grid
    print("\nGenerated Grid:")
    dfs_finder.print_grid()

    # Find the path using DFS
    path = dfs_finder.find_path()

    if path:
        print("\nPath found from source to destination:")
        for step in path:
            print(step)
    else:
        print("\nNo path found from source to destination.")
