import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

# Index (same behavior as df.reindex)
print(df.loc[pd.Index(["cobra", "viper"], name="foo")])
