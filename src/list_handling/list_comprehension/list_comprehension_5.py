matrix=[]

for i in range(3):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(f'The matrix with for-loop is:{matrix}')

matrix_1=[[j for j in range(5)] for i in range(3)]

print(f'The matrix with list comprehension is:{matrix_1}')