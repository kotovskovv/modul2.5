def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


n = int(input('Задайте количество строк матрицы    :'))
m = int(input('Задайте количество столбцов матрицы :'))
value = int(input(f'Задайте значения матрицы : '))
matrix = get_matrix(n, m, value)
print(matrix)

if n <= 0:
    print(matrix)
elif m <= 0:
    print(matrix)
else:
    print(matrix)




