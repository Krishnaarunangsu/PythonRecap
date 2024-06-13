import re

txt="hello planet"
# Check if the string starts with 'hello':
x=re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
  print(f'Matched Object:{x}')
else:
  print("No match")
