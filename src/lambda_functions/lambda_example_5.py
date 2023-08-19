# Lambda with List Comprehension
is_even_list= [lambda  arg=x: arg *10 for x in range(1,5)]
is_multiplication_list= [x*20 for x in range(1, 10)]


# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())

print('*******************************************')
for value in is_multiplication_list:
    print(value)

