# Create dataframe from List of dicts/dictionaries
# Import the library
import pandas as pd

# List of dictionaries
course_dict = [
        {
            'chapter': 1,
            'course': 'Data Science',
            'technology': 'Python'
        },
        {
            'chapter': 2,
            'course': 'Data Visualization',
            'technology': 'R'
        },
        {
            'chapter': 3,
            'course': 'Databases',
            'technology': 'SQL'
        }
    ]
# Create the Dataframe
course_dataframe = pd.DataFrame(data=course_dict)
print(f'The course dataframe is:\n:{course_dataframe}')
