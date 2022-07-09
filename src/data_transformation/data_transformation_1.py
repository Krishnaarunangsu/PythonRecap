import pandas as pd

df = pd.DataFrame({'A': range(3), 'B': range(1, 4)})
print(f'Original Data:\n{df}')

df = df.transform(lambda x: x + 1)
print(f'Modified Data:\n{df}')
