# Delete a Multiple Rows by Index Position in DataFrame
import pandas as pd

details_dict = {
    "Name": ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    "Age": [23, 21, 22, 21],
    "University": ['BHU', 'JNU', 'DU', 'BHU']
}

university_students_data = pd.DataFrame(details_dict, index=['a', 'b', 'c', 'd'])
print(university_students_data)

# return a new dataframe by dropping a row
# 'b' & 'c' from dataframe using their
# respective index position
update_df = university_students_data.drop([university_students_data.index[1], university_students_data.index[2]])
print(update_df)

