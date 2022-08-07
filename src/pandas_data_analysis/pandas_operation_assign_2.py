# Applying lambda function to multiple columns using Dataframe.assign()
import pandas as pd

# creating and initializing a nested list
volume_values_list = [
                        [15, 2.5, 100],
                        [20, 4.5, 50],
                        [25, 5.2, 80],
                        [45, 5.8, 48],
                        [40, 6.3, 70],
                        [41, 6.4, 90],
                        [51, 2.3, 111]
                     ]

columns = ['Length', 'Breadth', 'Height']

df = pd.DataFrame(volume_values_list, columns=columns)

print(f'Original Dataframe:\n{df}')

# # Applying lambda function to find the product of 3 columns using df.assign()
# Have a new calculated column "Volume" calculated from the "Total_Marks" column
df = df.assign(Volume=lambda x: (x['Length'] * x['Breadth'] * x['Height']))
print(f'Modified Dataframe:\n{df}')
