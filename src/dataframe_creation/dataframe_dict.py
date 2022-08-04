# Create dataframe from dict

# Import the library
import pandas as pd

# List of dictionaries
course_dict: dict = {
                        'chapter': 1,
                        'course': 'Data Science',
                        'technology': 'Python'
                    },

print((type(course_dict)))

# Create the Dataframe
course_dataframe = pd.DataFrame(data=course_dict)
print(f'The course dataframe is:\n{course_dataframe.dtypes}')
print(f'The course dataframe is:\n{type(course_dataframe)}')
