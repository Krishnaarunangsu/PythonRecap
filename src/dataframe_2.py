import pandas as pd

my_dict = [{'chapter': 1, 'course': 'Data Science', 'Technology': 'Python'},
           {'chapter': 2, 'course': 'Data Visualization', 'Technology': 'R'},
           {'chapter': 3, 'course': 'Databases', 'Technology': 'SQL'}]
datacamp = pd.DataFrame(my_dict)
print(datacamp['course'])
print('***************************************')
print(datacamp[['course']])
print('***************************************')
#print(datacamp[[['course']]])
datacamp.index = ["P", "Q", "R"]
print(datacamp)
