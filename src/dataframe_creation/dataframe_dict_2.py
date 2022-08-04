# Create dataframe from dict

# Import the library
import pandas as pd

# List of dictionaries
course_dict = {
            'chapter': 1,
            'course': 'Data Science',
            'technology': 'Python'
        }

# Create the Dataframe
course_dataframe = pd.DataFrame(data=course_dict)
print(f'The course dataframe is:\n{course_dataframe.dtypes}')
