class RobotTraversal:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.N = len(graph)  # Assuming a square grid
        self.M = len(graph[0])
        self.start = start  # Tuple (x, y) for starting point
        self.goal = goal    # Tuple (x, y) for goal point
        self.visited = set()  # Set to track visited nodes
        self.topological_order = []  # List to store topological order

        # Directions (Right, Left, Down, Up)
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(self, x, y):
        # Check if (x, y) is within bounds and not an obstacle
        return 0 <= x < self.N and 0 <= y < self.M and self.graph[x][y] == 1

    def dfs(self, x, y):
        # Mark the current node as visited
        self.visited.add((x, y))

        # Explore all 4 possible directions (Right, Left, Down, Up)
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy

            if (nx, ny) not in self.visited and self.is_valid(nx, ny):
                self.dfs(nx, ny)

        # Add the current node to the topological order after visiting all neighbors
        self.topological_order.append((x, y))

    def find_topological_order(self):
        # Start DFS from the start node
        self.dfs(self.start[0], self.start[1])

        # Reverse the topological order (because we visited the nodes in post-order)
        self.topological_order.reverse()
        return self.topological_order

# Example usage:
if __name__ == "__main__":
    # Grid where 1 represents open space and 0 represents an obstacle
    graph = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 0, 1]
    ]
    
    start = (0, 0)  # Starting point
    goal = (4, 4)   # Goal point

    robot = RobotTraversal(graph, start, goal)
    topological_order = robot.find_topological_order()

    print("Topological Order of Node Traversal:")
    for node in topological_order:
        print(node)
