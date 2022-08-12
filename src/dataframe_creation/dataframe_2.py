import pandas as pd

my_dict = [
    {'chapter': 1,
     'course': 'Data Science',
     'Fee': '3509',
     'Technology': 'Python'
     },
    {
        'chapter1': 2,
     'course': 'Data Visualization',
        'Technology': 'R'
    },
    {
        'chapter': 3,
        'course': 'Databases',
        'Technology': 'SQL',
        'Fee':'2500'
    }
]


datacamp = pd.DataFrame(my_dict, index=['A','B','C'])
print(datacamp)
print('********************************')
print(datacamp.dtypes)
print('********************************')
print(datacamp['course'])
print('***************************************')
print(datacamp[['course']])
print('***************************************')
# print(datacamp[[['course']]])
datacamp.index = ["P", "Q", "R"]
print(datacamp)
