# Traditional Approach

# Empty List
list_1=[]

for character in "Geeks 4 Geeks":
    list_1.append(character)

print(f'The List generated with  is:{list_1}')

# Using List Comprehension
list_2=[character for character in "Geeks 4 Geeks"]
print(f'The List generated with  is:{list_2}')