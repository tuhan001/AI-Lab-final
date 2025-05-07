from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.goal_found = False
        self.depth = 0
        self.max_depth = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def iddfs(self, start, goal):
        self.goal_found = False
        self.max_depth = 0

        while not self.goal_found:
            self.depth_limited_search(start, goal, 0, set())
            self.max_depth += 1

        print(f"\nGoal found at depth {self.depth}")

    def depth_limited_search(self, node, goal, current_depth, visited):
        if current_depth > self.max_depth:
            return

        visited.add(node)
        print(node, end="\t")

        if node == goal:
            self.goal_found = True
            self.depth = current_depth
            return

        for neighbor in self.graph[node]:
            if neighbor not in visited and not self.goal_found:
                self.depth_limited_search(neighbor, goal, current_depth + 1, visited)

def main():
    try:
        n = int(input("Enter number of nodes: "))
        e = int(input("Enter number of edges: "))

        g = Graph(n)

        print("Enter edges in the format 'u v' (without quotes):")
        for _ in range(e):
            u, v = map(int, input().split())
            g.add_edge(u, v)

        start = int(input("Enter the start node: "))
        goal = int(input("Enter the goal node: "))

        print("\nIDDFS Traversal:")
        g.iddfs(start, goal)

    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
