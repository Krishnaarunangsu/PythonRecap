# Use groupby() function to group the data based on the “Team”
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot', 'Sparrow', 'Falcon'],
        'Max Speed': [380., 370., 24., 26., 15, 27]
    }
)

print(f'Animal Speed Dataframe:\n{df}')

var = df.groupby('Animal').mean()
print(f'Average Speed of every group of animal:\n{var}')
