import re

txt="That will be 59 dollars"
# Find all digit characters
x=re.findall("\d", txt)
print(f'Matched Object:{x}')