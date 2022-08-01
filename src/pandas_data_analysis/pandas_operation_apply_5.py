# pandas apply()
# Documentation: https://sparkbyexamples.com/pandas/pandas-apply-function-usage-examples/#:~:text=7.-,Apply%20Lambda%20Function%20to%20Single%20Column,x%3Ax%2D2)%20.
import numpy as np
import pandas as pd

# creating and initializing a nested list
values_list = [[15, 2.5, 100], [20, 4.5, 50], [25, 5.2, 80],
               [45, 5.8, 48], [40, 6.3, 70], [41, 6.4, 90],
               [51, 2.3, 111]]
columns = ['Field_1', 'Field_2', 'Field_3']
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

df = pd.DataFrame(values_list, columns=columns, index=index)
print(f'Original Dataframe:\n{df}')


def add_4(x):
    """

    :param x:
    :return:
    """
    return x + 4


df['Field_2'] = df['Field_2'].apply(add_4)

print(f'Transformed Dataframe:\n{df}')
