import random
from collections import deque

class Node:
    def __init__(self, x, y, level, parent=None):
        self.x = x
        self.y = y
        self.level = level
        self.parent = parent  # Parent node to reconstruct the path

class BFS:
    def __init__(self, N, graph, start, goal):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]  # Directions for movement in x (down, up, right, left)
        self.y_move = [0, 0, 1, -1]  # Directions for movement in y (down, up, right, left)
        self.N = N
        self.graph = graph
        self.source = Node(start[0], start[1], 0)  # Initialize source node
        self.goal = Node(goal[0], goal[1], float('inf'))  # Initialize goal node
        self.found = False
        self.goal_level = None

    def st_bfs(self):
        q = deque([self.source])
        visited = [[False] * self.N for _ in range(self.N)]  # Track visited nodes
        visited[self.source.x][self.source.y] = True

        while q:
            u = q.popleft()

            for j in range(self.directions):
                v_x = u.x + self.x_move[j]
                v_y = u.y + self.y_move[j]

                if 0 <= v_x < self.N and 0 <= v_y < self.N and self.graph[v_x][v_y] == 1 and not visited[v_x][v_y]:
                    v_level = u.level + 1
                    if v_x == self.goal.x and v_y == self.goal.y:  # Goal check
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        self.goal.parent = u  # Set the parent of the goal to current node
                        return
                    visited[v_x][v_y] = True
                    child = Node(v_x, v_y, v_level, u)  # Set parent to current node
                    q.append(child)

    def print_path(self):
        if self.found:
            print("\nPath to goal:")
            path = []
            current_node = self.goal
            while current_node is not None:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.reverse()  # Reverse the path to show it from start to goal
            for step in path:
                print(step)
        else:
            print("\nGoal not found. No path exists.")

    def print_matrix(self):
        for row in self.graph:
            print(" ".join(str(cell) for cell in row))

def generate_grid(N, obstacle_probability=0.3):
    # Generate N×N matrix with random obstacles
    grid = [[1 if random.random() > obstacle_probability else 0 for _ in range(N)] for _ in range(N)]
    return grid

def main():
    N = int(input("Enter grid size N (e.g., 5 for 5x5 grid): "))
    
    # Generate a random grid with obstacles (0 for obstacle, 1 for open space)
    grid = generate_grid(N)
    
    # Display the generated grid
    print("\nGenerated Grid (1 = open, 0 = obstacle):")
    for row in grid:
        print(" ".join(str(cell) for cell in row))

    # Take user input for start and goal states
    start_x = int(input("\nEnter start x-coordinate (0 to N-1): "))
    start_y = int(input("Enter start y-coordinate (0 to N-1): "))
    goal_x = int(input("Enter goal x-coordinate (0 to N-1): "))
    goal_y = int(input("Enter goal y-coordinate (0 to N-1): "))

    # Ensure the start and goal positions are valid (not obstacles)
    while grid[start_x][start_y] == 0 or grid[goal_x][goal_y] == 0:
        print("\nStart or goal position is blocked by an obstacle. Please select different coordinates.")
        start_x = int(input("Enter start x-coordinate (0 to N-1): "))
        start_y = int(input("Enter start y-coordinate (0 to N-1): "))
        goal_x = int(input("Enter goal x-coordinate (0 to N-1): "))
        goal_y = int(input("Enter goal y-coordinate (0 to N-1): "))

    # Create a BFS object and perform BFS traversal
    bfs = BFS(N, grid, (start_x, start_y), (goal_x, goal_y))
    bfs.st_bfs()

    if bfs.found:
        print(f"\nGoal found! Number of moves required: {bfs.goal_level}")
        bfs.print_path()  # Print the path from start to goal
    else:
        print("\nGoal cannot be reached from the starting block.")

if __name__ == "__main__":
    main()
