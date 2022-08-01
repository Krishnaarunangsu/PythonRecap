from re import search

# 'foo123bar', 'foo456bar', '234baz', and 'qux678
str_1 = 'foo1.3bar'
# str_1 = 'foo456bar' Search Pattern: Consecutive 3 digits in the string Take a look at another regex metacharacter.
# The dot (.) metacharacter matches any character except a newline, so it functions like a wildcard:
search_pattern = '[0-9][0-9][0-9]'
search_match = search(pattern='1.3', string=str_1)
print(f'Status of the searched string:{search_match}')

# [0-9] matches any single decimal digit character—any character between '0' and '9', inclusive. The full expression
# [0-9][0-9][0-9] matches any sequence of three decimal digit characters. In this case, s matches because it contains
# three consecutive decimal digit characters, '123'.

str_2 = '34foo13bar'
search_match = search(pattern='1.3', string=str_2)
print(f'Status of the searched string:{search_match}')

