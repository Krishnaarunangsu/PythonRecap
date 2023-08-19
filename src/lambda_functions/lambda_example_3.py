# Define the lambda function
number_format=lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
# number_format=lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

number=input(f'Please Enter the number:')
print(f'Number Formatting:{number_format(float(number))}')

