import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import depth_first_order

arr_1 = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])

print(f'Original Numpy Array:\n{arr_1}')

arr_2 = csr_matrix(arr_1)

# Floyd Warshall
# Use the floyd_warshall() method to find shortest path between all pairs of elements.

depth_first_1 = depth_first_order(arr_2, 1)
print(f'Connection Weights:\n{depth_first_1}')

graph = [
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 0, 0, 0]
]
graph = csr_matrix(graph)
print(graph)

graph = [
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 3],
    [0, 0, 0, 0]
]
graph = csr_matrix(graph)
print(graph)
depth_2 = depth_first_order(graph, 0)
