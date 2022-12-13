import pandas as pd
import numpy as np

data = {
    "a": list(range(4)),
    "b": list("ab.."),
    "c": ["a", "b", np.nan, "d"]
}

df_1 = pd.DataFrame(data)
print(f'The Original Dataframe is:\n{df_1}')

# Replace . by NaN
print(f'The Dataframe after modification:\n{df_1.replace(".",np.nan)}')
