# list comprehension
doubles = [2 * n for n in range(50)]
# same as the list comprehension above
doubles = list(2 * n for n in range(50))
print(f'The list is:{doubles}')