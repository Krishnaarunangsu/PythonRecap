list_1 = []
list_1=[i for  i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]

print(f'Print the list divisible by 7 but not divisible by 5:{list_1}')
print('The numbers divisible by 7 but not divisible by 5')
# [print(f'{x}') for x in list_1]
