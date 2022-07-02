# Just adding another way for DataFrame expanded over all columns:
import pandas as pd

df = pd.DataFrame()

for column in df.columns:
    df = df[df[column] != 0]


def z_score(data, count):
    threshold = 3
    for column in data.columns:
        mean = np.mean(data[column])
        std = np.std(data[column])
        for i in data[column]:
            zscore = (i - mean) / std
            if (np.abs(zscore) > threshold):
                count = count + 1
                data = data[data[column] != i]
    return data, count
