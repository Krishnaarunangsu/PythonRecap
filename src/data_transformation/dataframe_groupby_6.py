import pandas as pd

df = pd.DataFrame(
    {
        'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot', 'Sparrow', 'Falcon'],
        'Max Speed': [380., 370., 24., 26., 70, 234]
    }
)

print(f'Animal Speed Dataframe:\n{df}')
# Average speed by Animal
animal_speed_average = df.groupby(['Animal']).mean()
print(f'Animal Average Speed:\n{animal_speed_average}')
