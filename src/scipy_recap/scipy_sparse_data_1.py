import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 2])
sparse_data = csr_matrix(arr)
print(f'The Sparse Data is:\n{sparse_data}')

# From the result we can see that there are 3 items with value.
# The 1. item is in row 0 position 5 and has the value 1.
# The 2. item is in row 0 position 6 and has the value 1.
# The 3. item is in row 0 position 8 and has the value 2.

# Viewing stored data (not the zero items) with the data property:
arr_2 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr_2).data)

# Counting non-zeros with the count_nonzero() method:
print(f'{csr_matrix(arr_2).count_nonzero()}')

# Removing zero-entries from the matrix with the eliminate_zeros() method:
arr_3 = csr_matrix(arr_2)
arr_3.eliminate_zeros()
print(arr_2)
print(arr_3)

# Converting from csr to csc with the tocsc() method:
arr_4 = csr_matrix(arr_2).tocsc()
print(arr_2)
print(arr_4)

# # Counting non-zeros with the count_nonzero() method:
arr_5 = np.array([[0, 10, 0], [0, 50, 1], [1, 0, 2]])
print(csr_matrix(arr_5).count_nonzero())

arr_6 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
matrix = csr_matrix(arr_6)
matrix.sum_duplicates()

# https://codingstreets.com/python-scipy-sparse-data/
