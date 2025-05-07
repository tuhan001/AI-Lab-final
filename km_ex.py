import random

# Constants
GRID_SIZE = 50  # Size of 2D matrix (50x50)
NUM_POINTS = 100
NUM_CLUSTERS = 10
DATA_FILE = "points.txt"

# Step 1: Generate the data file
def generate_data_file():
    with open(DATA_FILE, "w") as f:
        f.write("# Data Points\n")
        for _ in range(NUM_POINTS):
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            f.write(f"P {x} {y}\n")

        f.write("# Cluster Centers\n")
        for _ in range(NUM_CLUSTERS):
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            f.write(f"C {x} {y}\n")

# Step 2: Load data from file
def load_data():
    points = []
    clusters = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.startswith("#") or line.strip() == "":
                continue
            parts = line.strip().split()
            label, x, y = parts[0], int(parts[1]), int(parts[2])
            if label == 'P':
                points.append({'x': x, 'y': y, 'cluster': -1})
            elif label == 'C':
                clusters.append({'x': x, 'y': y})
    return points, clusters

# Step 3: Manhattan Distance
def manhattan(p1, p2):
    return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])

# Step 4: K-Means with Manhattan Distance
def k_means(points, clusters):
    while True:
        changed = False

        # Assign points to nearest cluster
        for p in points:
            min_dist = float('inf')
            best_cluster = -1
            for i, c in enumerate(clusters):
                d = manhattan(p, c)
                if d < min_dist:
                    min_dist = d
                    best_cluster = i
            if p['cluster'] != best_cluster:
                p['cluster'] = best_cluster
                changed = True

        if not changed:
            break

        # Recalculate cluster centers
        for i in range(len(clusters)):
            cluster_points = [p for p in points if p['cluster'] == i]
            if cluster_points:
                avg_x = sum(p['x'] for p in cluster_points) // len(cluster_points)
                avg_y = sum(p['y'] for p in cluster_points) // len(cluster_points)
                clusters[i]['x'] = avg_x
                clusters[i]['y'] = avg_y

# Step 5: 2D Grid Visualization
def print_grid(points, clusters):
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Place cluster centers (C1 to C10)
    for i, c in enumerate(clusters):
        grid[c['y']][c['x']] = chr(65 + i)  # A, B, C...

    # Place points
    for p in points:
        ch = chr(97 + p['cluster'])  # a, b, c... for clusters
        if grid[p['y']][p['x']] == '.':
            grid[p['y']][p['x']] = ch

    # Print the grid
    print("\n=== Clustered 2D Grid ===")
    for row in grid:
        print(' '.join(row))

# Run it all
if __name__ == "__main__":
    generate_data_file()
    points, clusters = load_data()
    k_means(points, clusters)
    print_grid(points, clusters)
