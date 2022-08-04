import numpy as np

numpy1 = np.array([17.2, 20.0, 8.25, 9.50])
numpy2 = np.array([13.0, 24.0, 8.25, 9.0])
print(np.logical_and(numpy1 > 10, numpy2 < 20))
