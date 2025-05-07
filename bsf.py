from collections import deque

class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level

class BFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]  # Directions for movement in x (down, up, right, left)
        self.y_move = [0, 0, 1, -1]  # Directions for movement in y (down, up, right, left)
        self.found = False
        self.goal_level = None
        self.source = None
        self.goal = None
        self.init()

    def init(self):
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]
        self.N = len(graph)

        source_x, source_y = 0, 2  # Source position
        goal_x, goal_y = 4, 4  # Goal position
        self.source = Node(source_x, source_y, 0)  # Initialize source node
        self.goal = Node(goal_x, goal_y, float('inf'))  # Initialize goal node with an unreachable level

        self.st_bfs(graph)

        if self.found:
            print("Goal found")
            print(f"Number of moves required = {self.goal_level}")
        else:
            print("Goal cannot be reached from the starting block")

    def st_bfs(self, graph):
        q = deque([self.source])
        visited = [[False] * self.N for _ in range(self.N)]  # Track visited nodes
        visited[self.source.x][self.source.y] = True

        while q:
            u = q.popleft()

            for j in range(self.directions):
                v_x = u.x + self.x_move[j]
                v_y = u.y + self.y_move[j]

                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1 and not visited[v_x][v_y]:
                    v_level = u.level + 1
                    if v_x == self.goal.x and v_y == self.goal.y:  # Goal check
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        return
                    visited[v_x][v_y] = True
                    child = Node(v_x, v_y, v_level)
                    q.append(child)

if __name__ == "__main__":
    bfs = BFS()
