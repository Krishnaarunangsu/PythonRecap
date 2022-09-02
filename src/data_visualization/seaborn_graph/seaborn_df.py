import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]

plot_data = pd.DataFrame(list(zip(x, y)),
               columns =['X', 'Y'])

print(plot_data)

sns.lineplot(x="X",
             y="Y",
             data=plot_data)  # using lineplot() function to create line plot

plt.show()
