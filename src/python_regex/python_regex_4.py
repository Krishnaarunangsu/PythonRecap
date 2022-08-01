# Metacharacters That Match a Single Character

# []: Specifies a specific set of characters to match. Characters contained in square brackets ([]) represent a
# character class—an enumerated set of characters to match from. A character class metacharacter sequence will match
# any single character contained in the class.

from re import search

str_1 = 'FOOzaedacr'
# Match any character between a and z, inclusive
search_pattern = '[a-z]'
search_match = search(pattern=search_pattern, string=str_1)
print(f'Status of the searched string:{search_match}')

