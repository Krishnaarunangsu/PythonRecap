# Triangulation A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can
# compute an area of the polygon. A Triangulation with points means creating surface composed triangles in which all
# the given points are on at least one vertex of any triangle in the surface. One method to generate these
# triangulations through points is the Delaunay() Triangulation.
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

print(points)

simplices = Delaunay(points).simplices

print(simplices)

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

# Note: The simplices property creates a generalization of the triangle notation.
plt.show()
