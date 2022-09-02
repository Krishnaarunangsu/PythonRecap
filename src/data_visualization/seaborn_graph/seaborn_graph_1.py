# Importing seaborn library in program
import seaborn as sns
# Importing mataplotlib library to show graph in output
import matplotlib.pyplot as plt

# Setting style with set() function
from pandas import DataFrame

sns.set(style="dark")
# Using dataset() function to declare data type
plot_data: DataFrame = sns.load_dataset("fmri")

# Plotting various responses for different\# Regions and events
sns.lineplot(x="timepoint",
             y="signal",
             hue="region",
             style="event",
             data=plot_data)  # using lineplot() function to create line plot

plt.show()  # using show() function
