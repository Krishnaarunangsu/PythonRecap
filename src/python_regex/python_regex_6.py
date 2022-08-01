# \ – Backslash
# The backslash (\) makes sure that the character is not treated in a special way. This can be
# considered a way of escaping metacharacters. For example, if you want to search for the dot(.) in the string then
# you will find that dot(.) will be treated as a special character as is one of the metacharacters (as shown in the
# above table). So for this case, we will use the backslash(\) just before the dot(.) so that it will lose its
# specialty. See the below example for a better understanding.


from re import search

# Without using \
str_1 = 'geeks.forgeeks'

search_match = search(pattern='.', string=str_1)
print(f'Status of the searched string:{search_match}')

# using \
search_match = search(pattern='\.', string=str_1)
print(f'Status of the searched string:{search_match}')

# Note: Here r character (r’portal’) stands for raw, not regex. The raw string is slightly different from a regular
# string, it won’t interpret the \ character as an escape character. This is because the regular expression engine
# uses \ character for its own escaping purpose.
