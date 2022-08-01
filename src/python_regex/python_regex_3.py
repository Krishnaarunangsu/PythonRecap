# Metacharacters That Match a Single Character

# []: Specifies a specific set of characters to match. Characters contained in square brackets ([]) represent a
# character class—an enumerated set of characters to match from. A character class metacharacter sequence will match
# any single character contained in the class.

from re import search

str_1 = 'foobarqux'

search_pattern = 'ba[artz]'
search_match = search(pattern=search_pattern, string=str_1)
print(f'Status of the searched string:{search_match}')

str_2 = 'foobazqux'
search_match = search(pattern=search_pattern, string=str_2)
print(f'Status of the searched string:{search_match}')
