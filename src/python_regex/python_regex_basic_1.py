# Imagine you have a string object str_1. Now suppose you need to write Python code to find out whether s contains
# the substring '123'. There are at least a couple ways to do this. You could use the in operator:

str_1 = 'foo123bar'
present: bool = '123' in str_1
print(f'String Matching Status:{present}')

# If you want to know not only whether '123' exists in s but also where it exists, then you can use .find() or .index().
# Each of these returns the character position within s where the substring resides:
location_find = str_1.find('123')
print(f'Location of the search string:{location_find}')

location_index = str_1.index('123')
print(f'Index of the search string:{location_index}')
