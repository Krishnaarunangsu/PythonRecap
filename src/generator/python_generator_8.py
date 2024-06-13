file_name="C:\\Arunangsu\\PythonRecap\\data\\annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
csv_gen = (row for row in open(file_name))
#print(next(csv_gen))
#print(next(csv_gen))

row_count=0
for i in csv_gen:
    row_count+=1

print(f'Total Rows:{row_count}')