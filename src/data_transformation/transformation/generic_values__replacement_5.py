import pandas as pd
import numpy as np

series_1 = pd.DataFrame([0.0, 1.0, 2.0, 3.0, 4.0])
print(f'The series is:\n{series_1}')
print(f'Modified Series after the replacement Operation:\n{series_1.replace([1, 2,3], method="pad")}')
