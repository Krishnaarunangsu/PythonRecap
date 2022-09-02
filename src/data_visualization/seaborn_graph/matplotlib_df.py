import matplotlib.pyplot as plt

# data to display on plots
x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]

# This will plot a simple bar chart
plt.plot(x, y)

# Title to the plot
plt.title("Line Chart")

# Adding the legends
plt.legend(["Line"])
plt.show()