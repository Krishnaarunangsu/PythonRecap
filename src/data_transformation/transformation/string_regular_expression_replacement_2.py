import pandas as pd
import numpy as np
import re

data = {
    "a": list(range(4)),
    "b": list("ab.."),
    "c": ["a", "b", np.nan, "d"]
}

df_1 = pd.DataFrame(data)
print(f'The Original Dataframe is:\n{df_1}')

# Replace . by NaN
print(df_1.replace(r"\s*\.\s*", np.nan, regex=True))


