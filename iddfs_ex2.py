from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.max_depth = 0
        self.path = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def iddfs(self, start, goal):
        self.max_depth = 0

        while True:
            visited = set()
            path = []
            found = self.dls(start, goal, 0, visited, path)
            if found:
                self.path = path
                return path
            self.max_depth += 1

    def dls(self, node, goal, current_depth, visited, path):
        if current_depth > self.max_depth:
            return False

        visited.add(node)
        path.append(node)

        if node == goal:
            return True

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.dls(neighbor, goal, current_depth + 1, visited, path):
                    return True

        path.pop()
        return False


def main():
    try:
        n = int(input("Enter number of nodes: "))
        e = int(input("Enter number of edges: "))

        g = Graph(n)

        print("Enter edges in the format 'u v':")
        for _ in range(e):
            u, v = map(int, input().split())
            g.add_edge(u, v)

        start = int(input("Enter the start node: "))
        goal = int(input("Enter the goal node: "))

        result = g.iddfs(start, goal)

        if result:
            print(f"\nPath from {start} to {goal} using IDDFS: {' -> '.join(map(str, result))}")
            print(f"Depth found: {len(result) - 1}")
        else:
            print("No path found.")

    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
