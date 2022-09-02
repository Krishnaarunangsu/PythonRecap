# Even though the resulting DataFrame must have the same length as the input DataFrame,
# it is possible to provide several input functions:

import pandas as pd

# Create a pandas Dataframe
df = pd.DataFrame(
    {
        "Date": [
            "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05",
            "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05"],
        "Data": [5, 8, 6, 1, 50, 100, 60, 120],
    }
)
print(f'Original Data:\n{df}')

df_group_by_sum = df.groupby('Date')['Data'].transform('count')
print(f'Modified Data:\n{df_group_by_sum}')
print(type(df_group_by_sum))

df_group_by_sum = df.groupby('Date')['Data'].transform('sum')
print(f'Modified Data:\n{df_group_by_sum}')
print(type(df_group_by_sum))

df_group_by_sum = df.groupby('Date')['Data'].transform(sum)
print(f'Modified Data:\n{df_group_by_sum}')
print(type(df_group_by_sum))


