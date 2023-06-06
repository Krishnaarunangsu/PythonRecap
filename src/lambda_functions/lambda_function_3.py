# filter the list items based on the condition
from functools import reduce

list_to_be_reduced=['Python','programming','is','awesome!']
list_reduced=reduce(
        lambda val1,val2:val1+" "+val2,
        list_to_be_reduced
    )
print(f'The filtered list is:{list_reduced}')