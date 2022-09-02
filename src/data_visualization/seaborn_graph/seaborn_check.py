import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

flights_data = sns.load_dataset("flights")
print(flights_data.head())

sns.lineplot(x='month', y='passengers', data=flights_data)
plt.show()