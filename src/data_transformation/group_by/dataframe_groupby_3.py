# Hierarchical Indexes: Use groupby() function to group the data based on the “Team”

import pandas as pd

animal_type_sub_type = [
                          ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
                          ['Captive', 'Wild', 'Captive', 'Wild']
                       ]

# Create 1st level and 2nd level index
index = pd.MultiIndex.from_arrays(arrays=animal_type_sub_type, names=('Animal', 'Type'))

# Create the dataframe
df = pd.DataFrame(
    {
        'Max Speed': [390., 350., 30., 20.]
    },
    index=index
)

print(f'Animal Speed Dataframe:\n{df}')

# Calculate mean/average speed by Animal
mean_speed_animal_type = df.groupby('Animal').mean()
print(f'Average Speed of every group of animal:\n{mean_speed_animal_type}')
