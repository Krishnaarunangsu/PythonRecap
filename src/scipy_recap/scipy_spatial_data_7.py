# Distance Matrix There are many Distance Metrics used to find various types of distances between two points in data
# science, Euclidean distance, cosine distance etc. The distance between two vectors may not only be the length of
# straight line between them, it can also be the angle between them from origin, or number of unit steps required
# etc. Many of the Machine Learning algorithm's performance depends greatly on distance metrics. E.g. "K Nearest
# Neighbors", or "K Means" etc. Let us look at some Distance Metrics:

# Hamming Distance
# Is the proportion of bits where two bits are difference.
# It's a way to measure distance for binary sequences.
from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)
print(f'Hamming Distance:{res}')
