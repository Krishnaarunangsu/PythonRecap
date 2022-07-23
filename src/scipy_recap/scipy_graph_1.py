import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

arr_1 = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

print(f'Original Numpy Array:\n{arr_1}')

arr_2 = csr_matrix(arr_1)

connection_weights = connected_components(arr_2)
print(f'Connection Weights:\n{connection_weights}')

# Dijkstra
# Use the dijkstra method to find the shortest path in a graph from one element to another.
# It takes following arguments:
# return_predecessors: boolean (True to return whole path of traversal otherwise False).
# indices: index of the element to return all paths from that element only.
# limit: max weight of path.


