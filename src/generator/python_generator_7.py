# def csv_reader(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

csv_gen = csv_reader("C:\\Arunangsu\\PythonRecap\\data"
                     "\\annual-enterprise-survey-2021-financial-year-provisional-csv.csv")

row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")