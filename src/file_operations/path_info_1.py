import os
from datetime import datetime

file_name=str(datetime.now().date())+'.txt'
print(file_name)
print(os.path.dirname(__file__))
file_path=os.path.join(os.path.dirname(__file__)+'\data'+file_name)

with open(file_path,'w') as f:
    f.write('ABCDE')