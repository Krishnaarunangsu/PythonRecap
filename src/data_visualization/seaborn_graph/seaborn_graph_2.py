# importing numpy as np library module
import numpy as np
# Importing seaborn library in program
import seaborn as sns
# Importing mataplotlib library to show graph in output
import matplotlib.pyplot as plt

# Selecting style for boxplot with set() function
sns.set(style="white")

# Generate a random univariate type distribution
random_univariate_distribution = np.random.RandomState(10)
plot_data = random_univariate_distribution.normal(size=100)
# Plotting a simple histogram with kdeplot variation
sns.histplot(plot_data, kde=True, color="m")
plot = sns.histplot(plot_data, kde=True, color="m")
print(plot)

# Display the Graph
plt.show()  # using show() function
