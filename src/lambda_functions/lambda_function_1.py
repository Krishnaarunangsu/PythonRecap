# filter the list items based on the condition
list_to_be_filtered=['Python','programming','is','awesome!']
list_filtered=list(
    filter(
        lambda arg:len(arg)<8,
        list_to_be_filtered
    )
)
print(f'The filtered list is:{list_filtered}')