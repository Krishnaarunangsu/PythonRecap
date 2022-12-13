import pandas as pd
import numpy as np

df_1 = pd.DataFrame({"a":[0.0, 1.0, 2.0, 3.0, 4.0], "b":[5, 6, 7, 8, 9]})
print(f'The series is:\n{df_1}')
print(f'Modified dataframe after the replacement Operation:\n{df_1.replace({"a":0,"b":5}, 100)}')
