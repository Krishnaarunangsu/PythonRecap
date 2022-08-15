# Python program to demonstrate
# array creation techniques
import numpy as np

tuple_1 = (1, 3, 2)

# Creating array from tuple
numpy_array_1 = np.array(
             tuple_1,
             dtype=int
            )
print("\nArray created using passed tuple:\n", numpy_array_1)
