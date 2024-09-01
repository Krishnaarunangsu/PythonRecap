import pandas as pd

student_performance_data="C://Arunangsu//PythonRecap//data//csv//student_performance_Data.csv"
# Creating a Dataframe
df = pd.read_csv(student_performance_data)
print(f'Data Summary:\n{df.head()}')

# Group By
def max_hours_per_gender_major(data):
    """
    Find the highest total study hours per week
    for each major and for each gender
    Args:
        data:

    Returns:


    """
    # Group data by gender and major and sum study hours
    grouped_data=data.groupby(['Gender', 'Major'])['StudyHoursPerWeek'].sum()
    print(f'Sum of Study Hours:\n{grouped_data}')
    top_categories_1=grouped_data.groupby(level=0).idxmax()
    print(f'Top Categories of Each Gender and Each Major:\n{top_categories_1}')
    print('***************************************************************************')
    #top_categories_2=df.groupby(['Gender','Major'])['StudyHoursPerWeek'].idxmax()
    #print(f'Top Categories of Each Gender and Each Major:\n{top_categories_2}')
    result = data.groupby(['Gender', 'Major']).agg({'StudyHoursPerWeek': 'sum'})
    print(result)
    print('***************************************************************************')
    top_categories_2 = result.groupby(['Gender','Major'])['StudyHoursPerWeek'].idxmax()
    print(f'Top Categories of Each Gender and Each Major:\n{top_categories_2}')
    print('***************************************************************************')
    top_categories_3 = result.groupby(['Gender'])['StudyHoursPerWeek'].idxmax()
    print(f'Top Categories of Each Gender:\n{top_categories_3}')
    print('***************************************************************************')

max_hours_per_gender_major(df)