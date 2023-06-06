matrix_1=[i*10 for i in range(1,6)]

print(f'The matrix is:{matrix_1}')

matrix_2=list(map(lambda i:i*10,[i for i in range(1,6)]))
print(f'The matrix is:{matrix_2}')
