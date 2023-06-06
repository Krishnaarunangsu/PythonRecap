# Display Transpose of 2D- Matrix.
# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
list_1=[[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]
print(list_1)