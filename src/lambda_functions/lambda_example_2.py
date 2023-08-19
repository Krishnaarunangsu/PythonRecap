# Define the lambda function
number_format=lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
# number_format=lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print(f'Integer Formatting:{number_format(1000000000)}')
print(f'Float Formatting:{number_format(8798.7643)}')
