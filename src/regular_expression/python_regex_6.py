import re

txt="hello planet"
# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x=re.findall("he.*o", txt)
if x:
  print("Yes, the string ends with 'planet'")
  print(f'Matched Object:{x}')
else:
  print("No match")
