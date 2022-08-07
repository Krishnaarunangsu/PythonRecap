import pandas as pd

my_dataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

my_var = pd.DataFrame(my_dataset)

print(f'Dataframe from List:\n{my_var}')

# List of dictionaries
my_data = [
    {'car': 'BMW', 'passing': 3},
    {'car': 'Volvo', 'passing': 7},
    {'car': 'Ford', 'passing': 2}
]

my_dataset_2 = pd.DataFrame(my_data)

print(f'Dataframe from JSON:\n{my_dataset_2}')
