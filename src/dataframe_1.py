import pandas as pd

datacamp = pd.DataFrame([{'chapter': 1, 'course': 'Data Science', 'technology': 'Python'},
                         {'chapter': 2, 'course': 'Data Visualization', 'technology': 'R'},
                         {'chapter': 3, 'course': 'Databases', 'technology': 'SQL'}])

print(datacamp[1:3])
