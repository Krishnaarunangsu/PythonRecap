# KDTrees
# KDTrees are a datastructure optimized for nearest neighbor queries.
# E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.
# The KDTree() method returns a KDTree object.
# The query() method returns the distance to the nearest neighbor and the location of the neighbors.

# Find the nearest neighbor to point (1,1):
from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)

res = kdtree.query((1, 1))

print(res)
