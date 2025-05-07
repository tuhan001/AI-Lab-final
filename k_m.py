import random
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

    def set_cluster(self, c):
        self.cluster = c

class KMeans:
    def __init__(self, num_points, num_clusters):
        self.num_points = num_points
        self.num_clusters = num_clusters
        self.points = []
        self.centroids = []
        self.cluster_points = []
        self.run()

    def generate_points(self):
        self.points = [Point(random.randint(0, self.num_points),
                             random.randint(0, self.num_points)) for _ in range(self.num_points)]

    def generate_centroids(self):
        self.centroids = [Point(random.randint(0, self.num_points),
                                random.randint(0, self.num_points)) for _ in range(self.num_clusters)]

    def assign_clusters(self):
        for p in self.points:
            min_dist = float('inf')
            for i, c in enumerate(self.centroids):
                dist = math.sqrt((c.x - p.x) ** 2 + (c.y - p.y) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    p.set_cluster(i)

    def update_centroids(self):
        new_centroids = []
        for i in range(self.num_clusters):
            x_sum = y_sum = count = 0
            for p in self.points:
                if p.cluster == i:
                    x_sum += p.x
                    y_sum += p.y
                    count += 1
            if count > 0:
                new_centroids.append(Point(x_sum // count, y_sum // count))
            else:
                # If no points are assigned to the cluster, keep it the same
                new_centroids.append(self.centroids[i])
        return new_centroids

    def compute_error(self, new_centroids):
        err = 0
        for old, new in zip(self.centroids, new_centroids):
            err += abs(old.x - new.x) + abs(old.y - new.y)
        return err

    def compute_intra_distances(self):
        for i in range(self.num_clusters):
            intra_distance = 0
            for p in self.points:
                if p.cluster == i:
                    intra_distance += math.sqrt((self.centroids[i].x - p.x) ** 2 +
                                                (self.centroids[i].y - p.y) ** 2)
            print(f"Cluster {i + 1} Intra-distance = {intra_distance:.2f}")

    def print_clusters(self):
        for i in range(self.num_clusters):
            for p in self.points:
                if p.cluster == i:
                    print(f"Point ({p.x}, {p.y}) -> Cluster {i + 1}")

    def group_clusters(self):
        self.cluster_points = [[] for _ in range(self.num_clusters)]
        for p in self.points:
            self.cluster_points[p.cluster].append(p)

    def run(self):
        self.generate_points()
        self.generate_centroids()

        while True:
            self.assign_clusters()
            new_centroids = self.update_centroids()
            error = self.compute_error(new_centroids)
            self.centroids = new_centroids
            if error == 0:
                break

        self.compute_intra_distances()
        self.print_clusters()
        self.group_clusters()


if __name__ == "__main__":
    num_points = int(input("Insert number of points: "))
    num_clusters = int(input("Insert number of clusters: "))
    kmeans = KMeans(num_points, num_clusters)
