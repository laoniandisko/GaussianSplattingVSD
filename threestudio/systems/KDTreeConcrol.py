import numpy as np
from scipy.spatial import KDTree

class KDTreeNearestNeighbor:
    def __init__(self, points):
        self.tree = KDTree(points)
        self.points = points

    def nearest_neighbor(self, point):
        _, idx = self.tree.query(point)
        return self.points[idx]

class OutlierRemoval:
    def __init__(self, points, epsilon, min_pts):
        self.points = points
        self.epsilon = epsilon
        self.min_pts = min_pts
        self.tree = KDTree(points)

    def remove_outliers(self):
        core_points = set()
        for i, point in enumerate(self.points):
            if len(self.tree.query_ball_point(point, self.epsilon)) >= self.min_pts:
                core_points.add(i)
        
        clusters = []
        visited = set()
        for core_point in core_points:
            if core_point not in visited:
                cluster = self._expand_cluster(core_point, visited, core_points)
                clusters.append(cluster)
        
        outliers = set(range(len(self.points))) - set.union(*clusters)
        filtered_points = np.array([self.points[i] for i in range(len(self.points)) if i not in outliers])
        return filtered_points, outliers

    def _expand_cluster(self, core_point, visited, core_points):
        cluster = set()
        queue = [core_point]
        while queue:
            point_idx = queue.pop()
            if point_idx not in visited:
                visited.add(point_idx)
                cluster.add(point_idx)
                neighbors = self.tree.query_ball_point(self.points[point_idx], self.epsilon)
                if len(neighbors) >= self.min_pts:
                    queue.extend([n for n in neighbors if n in core_points and n not in visited])
        return cluster

# Example usage
points = np.random.rand(100, 3)  # Replace with your actual point cloud data
epsilon = 0.1
min_pts = 5

outlier_removal = OutlierRemoval(points, epsilon, min_pts)
filtered_points, outliers = outlier_removal.remove_outliers()

print("Filtered points:", filtered_points)
print("Outliers:", outliers)
