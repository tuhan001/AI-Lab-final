from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def iddfs_topological_sort(self):
        # Initially, no node is visited
        visited = set()
        result = []

        # Perform IDDFS for topological sort
        for depth in range(self.V):
            visited.clear()
            temp_result = []
            if self.depth_limited_search(0, depth, visited, temp_result):
                result = temp_result
                break

        return result

    def depth_limited_search(self, node, max_depth, visited, result):
        # If max depth exceeded, return False
        if max_depth < 0:
            return False

        # Mark the current node as visited
        visited.add(node)

        # Add the node to the topological order result
        result.append(node)

        # Explore all neighbors
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if not self.depth_limited_search(neighbor, max_depth - 1, visited, result):
                    return False

        return True

def main():
    try:
        n = int(input("Enter the number of nodes: "))
        e = int(input("Enter the number of edges: "))

        g = Graph(n)

        print("Enter edges in the format 'u v':")
        for _ in range(e):
            u, v = map(int, input().split())
            g.add_edge(u, v)

        print("\nTopological sort using IDDFS:")
        result = g.iddfs_topological_sort()
        
        if result:
            print("Topological order:", " -> ".join(map(str, result)))
        else:
            print("Topological sort not possible for the given graph.")

    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
