import pandas as pd

brand_data = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

print(f'Brand Data:\n{brand_data}')

# By default, it removes duplicate rows based on all columns.
brand_data_non_dup = brand_data.drop_duplicates()
print(f'Brand Data without duplicates:\n{brand_data_non_dup}')

# To remove duplicates on specific column(s), use subset.
brand_data_non_dup_brand = brand_data.drop_duplicates(subset=['brand'])
print(f'Brand Data without duplicates:\n{brand_data_non_dup_brand}')

# To remove duplicates and keep last occurrences, use keep.
brand_data_non_dup_last_occur = brand_data.drop_duplicates(subset=['brand', 'style'], keep='last')
print(f'Brand Data without duplicates:\n{brand_data_non_dup_brand}')

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
