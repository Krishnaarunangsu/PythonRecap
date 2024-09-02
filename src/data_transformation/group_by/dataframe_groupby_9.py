# Using groupby() and apply()
import pandas as pd

student_performance_data="C://Arunangsu//PythonRecap//data//csv//student_performance_Data.csv"
# Creating a Dataframe
df = pd.read_csv(student_performance_data)
print(f'Data Summary:\n{df.head()}')

# Group By

def get_max_study_hours(data):
    """

    Args:
        data:

    Returns:

    """
    return data.loc[data['StudyHoursPerWeek'].idxmax()]
def max_hours_per_gender_major(data):
    """
    Find the highest total study hours per week
    for each major and for each gender
    Args:
        data:

    Returns:


    """
    # Group data by gender and major and sum study hours
    max_study_hours=data.groupby(['Gender', 'Major']).apply(get_max_study_hours)
    print(max_study_hours)
    print('************************************************')
    # grouped_data = data.groupby(['Gender', 'Major'])['StudyHoursPerWeek'].sum()
    result = data.groupby(['Gender', 'Major']).agg({'StudyHoursPerWeek': 'sum'})
    sum_max_study_hours_gender_major=result.groupby(['Gender', 'Major']).apply(get_max_study_hours)
    print(sum_max_study_hours_gender_major)
    print('************************************************')
    sum_max_study_hours_gender = result.groupby(['Gender']).apply(get_max_study_hours)
    print(sum_max_study_hours_gender)


max_hours_per_gender_major(df)