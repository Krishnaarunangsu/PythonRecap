# Metacharacters That Match a Single Character

# []: Specifies a specific set of characters to match. Characters contained in square brackets ([]) represent a
# character class—an enumerated set of characters to match from. A character class metacharacter sequence will match
# any single character contained in the class.

from re import search

# str_1 = 'GeeksforGeeks: A computer science portal for geeks'
str_1 = r'GeeksforGeeks: A computer science portal for geeks'

search_match = search(pattern='portal', string=str_1)
print(f'Status of the searched string:{search_match}')

print(f'Start Index:{search_match.start()}')
print(f'End Index:{search_match.end()}')

# Note: Here r character (r’portal’) stands for raw, not regex. The raw string is slightly different from a regular
# string, it won’t interpret the \ character as an escape character. This is because the regular expression engine
# uses \ character for its own escaping purpose.

