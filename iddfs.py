class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.depth = 0
        self.max_depth = 0
        self.goal_found = False

    def iterative_deepening(self, adjacency_matrix, destination):
        self.number_of_nodes = len(adjacency_matrix) - 1
        self.max_depth = 0

        while not self.goal_found:
            self.depth_limited_search(adjacency_matrix, 1, destination)
            self.max_depth += 1

        print(f"\nGoal Found at depth {self.depth}")

    def depth_limited_search(self, adjacency_matrix, source, goal):
        visited = [0] * (self.number_of_nodes + 1)
        self.stack = [source]
        visited[source] = 1
        self.depth = 0

        print(f"\nAt Depth {self.max_depth}")
        print(source, end="\t")

        while self.stack:
            element = self.stack[-1]
            child_found = False

            for destination in range(1, self.number_of_nodes + 1):
                if (adjacency_matrix[element][destination] == 1 and
                    visited[destination] == 0 and
                    self.depth < self.max_depth):

                    self.stack.append(destination)
                    visited[destination] = 1
                    self.depth += 1
                    print(destination, end="\t")

                    if destination == goal:
                        self.goal_found = True
                        return

                    child_found = True
                    break

            if not child_found:
                self.stack.pop()
                self.depth -= 1


def main():
    try:
        number_of_nodes = int(input("Enter the number of nodes in the graph: "))
        adjacency_matrix = [[0] * (number_of_nodes + 1) for _ in range(number_of_nodes + 1)]

        print("Enter the adjacency matrix:")
        for i in range(1, number_of_nodes + 1):
            row = list(map(int, input().split()))
            for j in range(1, number_of_nodes + 1):
                adjacency_matrix[i][j] = row[j - 1]

        destination = int(input("Enter the destination node: "))

        iddfs = IterativeDeepening()
        iddfs.iterative_deepening(adjacency_matrix, destination)

    except ValueError:
        print("Wrong input format")


if __name__ == "__main__":
    main()
