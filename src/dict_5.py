import pandas as pd

my_dict = [{'chapter': 1, 'course': 'python', 'level': 'advanced'},
           {'chapter': 2, 'course': 'r', 'level': 'intermediate'},
           {'chapter': 3, 'course': 'sql', 'level': 'beginner'}]

dataframe = pd.DataFrame(my_dict)
print(dataframe)

is_less = dataframe['chapter'] < 3
print(is_less)
print(dataframe[is_less])
