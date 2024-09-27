# Using groupby() and transform()
import pandas as pd

student_performance_data="C://Arunangsu//PythonRecap//data//csv//student_performance_Data.csv"
file_storage_path="C://Arunangsu//PythonRecap//data//csv//"
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
    max_study_hours = data.loc[data.groupby(['Gender', 'Major'])['StudyHoursPerWeek'].transform(max)==data['StudyHoursPerWeek']]
    print(f'Max Study Hours:\n{max_study_hours}')
    # Columns in the new Dataframe
    #print(f'Columns:\n{max_study_hours.columns}')
    # Drop the StudentID column from the new Dataframe
    max_study_hours_updated=max_study_hours.drop(['StudentID'], axis=1)
    print(f'After Dropping StudentID Column:\n{max_study_hours_updated}')
    #Write the new Dataframe to a CSV file
    max_study_hours_updated.to_csv(f'{file_storage_path}//studyHours.csv',sep='\t',index=False,encoding='utf-8')

    # Using DataFrame.drop
    #df.drop(df.columns[[1, 2]], axis=1, inplace=True)
    #data.drop(['StudentID'], axis=1, inplace=True)
    #print(f'Max Study Hours Result:\n{data}')
    # drop by Name
    #df1 = df1.drop(['B', 'C'], axis=1)
    #max_study_hours=max_study_hours.drop(['StudentID'], axis=1)
    # Select the ones you want
    #df1 = df[['a', 'd']]
    print('************************************************')
    # Sum the Study Hours Per Week for Each Gender and Each Major
    result = data.groupby(['Gender', 'Major']).agg({'StudyHoursPerWeek': 'sum'})
    print(f'1. Sum of Study Hours Per Week for Each Gender and Each Major:\n{result}')
    sum_max_study_hours_gender_major=result.loc[result.groupby(['Gender', 'Major'])['StudyHoursPerWeek'].transform(max)==result['StudyHoursPerWeek']]
    print(f'2. Sum of Study Hours Per Week for Each Gender and Each Major:\n{sum_max_study_hours_gender_major}')
    print('************************************************')
    sum_max_study_hours_gender = result.loc[result.groupby(['Gender'])['StudyHoursPerWeek'].transform(max)==result['StudyHoursPerWeek']]
    print(f'Sum of Study Hours Per Week for Each Gender:\n{sum_max_study_hours_gender}')


max_hours_per_gender_major(df)


# https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
# https://stackoverflow.com/questions/14940743/selecting-excluding-sets-of-columns-in-pandas