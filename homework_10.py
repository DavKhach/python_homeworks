matrix = [[x + y for x in range(3)] for y in  range(0, 9, 3)]

for i in matrix:
    for j in i:
        print(j, end= ' ')
    print(' ')


transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in transposed:
    print(row)




"""
matrix = matrix[::-1]

for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]

for row in matrix:
    print(row)
"""
