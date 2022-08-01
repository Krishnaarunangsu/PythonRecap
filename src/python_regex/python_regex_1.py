from re import search

# 'foo123bar', 'foo456bar', '234baz', and 'qux678
str_1 = 'foo123bar'
# str_1 = 'foo456bar'
search_match = search(pattern='123', string=str_1)
print(f'Status of the searched string:{search_match}')

if search_match:
    print("String is present")
else:
    print('String is not present')

print(str_1[3:6])
