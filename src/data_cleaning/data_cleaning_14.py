# Delete rows from dataFrame in Place
import pandas as pd

details_dict = {
    "Name": ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    "Age": [23, 21, 22, 21],
    "University": ['BHU', 'JNU', 'DU', 'BHU']
}

university_students_data = pd.DataFrame(details_dict, index=['a', 'b', 'c', 'd'])
print(university_students_data)

# dropping a row 'c' & 'd' from actual dataframe
university_students_data.drop(['c', 'd'], inplace=True)
print(university_students_data)
