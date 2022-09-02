import pandas as pd

list_1 = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
columns = ["a", "b", "c"]

df = pd.DataFrame(list_1, columns=columns)
print(f'Original Dataframe:\n{df}')

print(df.groupby(by=["b"]).sum())
print('**************************************************')
print(df.groupby(by=["b"], dropna=False).sum())
