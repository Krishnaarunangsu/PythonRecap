# filter the list items based on the condition
list_to_be_upper=['Python','programming','is','awesome!']
list_upper=list(
    map(
        lambda arg:arg.upper(),
        list_to_be_upper
    )
)
print(f'The filtered list is:{list_upper}')