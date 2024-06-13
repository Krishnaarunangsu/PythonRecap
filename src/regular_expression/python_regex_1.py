import re

txt="The rain in Spain"
# Search the string to see if it starts with "The" and ends with "Spain":
x=re.search("^The.*Spain$", txt)
print(f'Matched Object:{x}')