import pandas as pd
from matplotlib import pyplot as plt

flights=pd.read_csv("flights.csv")
print(flights.columns)

plt.plot(flights['month'], flights['passengers'])
plt.xlabel('year')
plt.ylabel('passengers')
plt.show()