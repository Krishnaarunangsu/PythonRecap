import re

txt="hello planet"
# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x=re.findall("he..o", txt)
print(f'Matched Object:{x}')