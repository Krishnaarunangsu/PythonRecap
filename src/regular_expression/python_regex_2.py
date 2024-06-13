import re

txt="The rain in Spain"
# Find all lowercase characters alphabetically between "a" and "m"
x=re.findall("[a-m]", txt)
print(f'Matched Object:{x}')