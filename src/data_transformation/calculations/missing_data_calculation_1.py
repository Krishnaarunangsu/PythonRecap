import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=["a", "c", "e", "f", "h"],
    columns=["one", "two", "three"],
)
print(f'The Original Dataframe is:\n{df}')
print('*********************************************')
print(df.loc['a', 'one'])
print('*********************************************')
df.loc['a', 'one'] = np.nan
print(f'The Modified Dataframe is:\n{df}')
