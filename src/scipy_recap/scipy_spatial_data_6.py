# Distance Matrix There are many Distance Metrics used to find various types of distances between two points in data
# science, Euclidean distance, cosine distance etc. The distance between two vectors may not only be the length of
# straight line between them, it can also be the angle between them from origin, or number of unit steps required
# etc. Many of the Machine Learning algorithm's performance depends greatly on distance metrics. E.g. "K Nearest
# Neighbors", or "K Means" etc. Let us look at some Distance Metrics:

# Cosine Distance
# Is the value of cosine angle between the two points A and B.
from scipy.spatial.distance import cosine

p1 = (1, 0)
p2 = (10, 2)

res = cosine(p1, p2)

print(f'Cosine Distance:{res}')
