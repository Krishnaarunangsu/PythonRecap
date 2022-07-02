import pandas as pd

my_dict = [{'device': 'X', 'price': 250, 'store': 'A'},
           {'device': 'Y', 'price': 200, 'store': 'A'},
           {'device': 'Z', 'price': 300, 'store': 'B'},
           {'device': 'X', 'price': 275, 'store': 'B'},
           {'device': 'Y', 'price': 250, 'store': 'C'},
           {'device': 'Z', 'price': 350, 'store': 'C'}]

print(my_dict)
df = pd.DataFrame(my_dict)
print(df)
print(df[df['store'] == 'A'])
