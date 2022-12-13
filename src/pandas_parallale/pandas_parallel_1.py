import pandas as pd
import numpy as np
from pandarallel import pandarallel

df =  pd.DataFrame(
    {
        "a":np.random.randint(0, 100, size=10000),
        "b":np.random.randint(0, 100, size=10000),
        "c":np.random.randint(0, 100, size=10000)
    }
)
pandarallel.initialize(progress_bar=True)
df.parallel_apply(lambda x: x**2)