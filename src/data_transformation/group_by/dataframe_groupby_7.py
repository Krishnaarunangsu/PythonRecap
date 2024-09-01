import pandas as pd

student_info={
    'Student':['Alice', 'Bob','Alice', 'Bob'],
    'Subject':['Math', 'Math', 'Science', 'Science'],
    'Grade':[90, 85, 88,92]
}
# Creating a Dataframe
df = pd.DataFrame(student_info)

# Group By Subject and calculate the average grade
# grouped_data=df.groupby('Subject').mean()
grouped_data=df.groupby('Subject')['Grade'].mean()
print(f'Average Grade of each subject:\n{grouped_data}')

# print(f'Animal Speed Dataframe:\n{df}')
# # Average speed by Animal
# animal_speed_average = df.groupby(['Animal']).mean()
# print(f'Animal Average Speed:\n{animal_speed_average}')
