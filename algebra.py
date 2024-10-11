import numpy as np

# Read input
n = int(input())  # Size of the matrix
matrix = []

# Read the matrix elements
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert list to numpy array
matrix = np.array(matrix)

# Calculate determinant
determinant = np.linalg.det(matrix)

# Print the determinant rounded to 2 decimal places
print(round(determinant, 2))
