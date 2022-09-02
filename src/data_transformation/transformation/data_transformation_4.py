# Even though the resulting DataFrame must have the same length as the input DataFrame,
# it is possible to provide several input functions:

import pandas as pd

# Create a pandas Dataframe
df = pd.DataFrame(
    {
        "c": [1, 1, 1, 2, 2, 2, 2],
        "type": ["m", "n", "o", "m", "m", "n", "n"]
    }
)
print(f'Original Data:\n{df}')

df['size'] = df.groupby('c')['type'].transform(len)
print(f'Modified Data:\n{df}')
print(type(df))




