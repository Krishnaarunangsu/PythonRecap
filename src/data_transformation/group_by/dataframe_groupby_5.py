import pandas as pd

list_1 = [["a", 12, 12], [None, 12.3, 33.], ["b", 12.3, 123], ["a", 1, 1]]
columns = ["a", "b", "c"]
df = pd.DataFrame(list_1, columns=columns)
print(f'Original Dataframe:\n{df}')
print('*********************************************')
print(f'Sum by Column a:\n{df.groupby(by="a").sum()}')
print('*********************************************')
print(f'{df.groupby(by="a", dropna=False).sum()}')
