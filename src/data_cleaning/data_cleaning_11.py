# Drop rows in Pandas DataFrame by index labels
import pandas as pd

details_dict = {
    "Name": ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    "Age": [23, 21, 22, 21],
    "University": ['BHU', 'JNU', 'DU', 'BHU']
}

university_students_data = pd.DataFrame(details_dict, index=['a', 'b', 'c', 'd'])
print(university_students_data)

index_university_student_data = university_students_data.index
print(index_university_student_data)

# return a new dataframe by dropping a
# row 'c' from dataframe
update_df = university_students_data.drop('c')
print(update_df)

for i in index_university_student_data:
    print(i)
    if i == 'c':
        print('Label is c')
        university_students_data.drop('c')
        print(university_students_data)
        university_students_data.drop('c', inplace=True)
        print(university_students_data)
