def create_zero_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]
def create_identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]
zero_matrix = create_zero_matrix(4, 5)
print("Zero Matrix of order 4x5:")
for row in zero_matrix:
    print(row)
identity_matrix = create_identity_matrix(5)
print("\nIdentity Matrix of order 5:")
for row in identity_matrix:
    print(row)
