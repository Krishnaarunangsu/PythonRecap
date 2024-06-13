import re

txt="hello planet"
# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x=re.findall("he.?o", txt)
if x:
  print("Yes, the string ends with 'planet'")
  print(f'Matched Object:{x}')
else:
  print("No match")