def create_matrix_with_value(size, value):
    return [[value for _ in range(size)] for _ in range(size)]
matrix = create_matrix_with_value(5, 10)
print("Matrix of order 5 with all entries as 10:")
for row in matrix:
    print(row)