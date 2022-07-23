import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

arr_1 = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

print(f'Original Numpy Array:\n{arr_1}')

arr_2 = csr_matrix(arr_1)

# Floyd Warshall
# Use the floyd_warshall() method to find shortest path between all pairs of elements.

floyd_1 = floyd_warshall(arr_2, return_predecessors=True)
print(f'Connection Weights:\n{floyd_1}')


