"""
Creating 2-Dimensional Arrays using Python lists
A list is a one dimensional object
We can use lists to create two dimensional objects
"""
"""
e.g. 4 x 3 matrix
1 2 3
4 5 6
7 8 9
10 11 12
"""
import random as matrix_numbers

matrix = list()

# Method 1 of reading the matrix dimensions
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

"""
# Method 2 of reading the matrix dimensions
dimensions = input("Enter the rows and the columns: ").split()
dimensions = [int(dimension) for dimension in dimensions]
rows = dimensions[0]
columns = dimensions[1]

# Method 3 of reading the matrix dimensions
rows, columns = input("Enter the rows and the columns: ").split()
print(rows, columns)
rows = int(rows)
columns = int(columns)
"""

print(f"So! You want to print a {rows} rows, {columns} columns matrix?")

start = 1
stop = 1
for row in range(rows):
    start = stop
    stop += columns
    line = [n for n in range(start, stop)]
    matrix.append(line)
print(f"Full matrix: {matrix}\n")

# Print / format the 2-D matrix
for row in range(rows):
    print()
    for column in range(columns):
        print(f"{matrix[row][column]:<6}", end=" ")


# Generate another matrix containing random numbers
matrix2 = []
for row in range(rows):
    line = [matrix_numbers.randint(100, 10000) for n in range(columns)]
    matrix2.append(line)

# Print / format the 2-D matrix
print(f"\n\nMatrix #2")
for row in range(rows):
    print()
    for column in range(columns):
        print(f"{matrix2[row][column]:<6}", end=" ")

# Multiplication of two matrices A and B.
# Example of two matrices (2x3) and (3x2)

matrix_A_rows = 2
matrix_A_columns = 3
matrix_B_rows = 3
matrix_B_columns = 2

matrix_A = list()
matrix_B = list()
matrix_C = list() # Initialize matrix C first!
"""
e.g of initialized matrix C of 4 x2
0 0
0 0
0 0
0 0
"""
for row in range(matrix_A_rows):
    for column in range(matrix_B):
        for coefficient in range(matrix_A_columns):
            # Multiply the coefficients in matrix_A and matrix_B and store the result in matrix C
            matrix_C[row][column] = ...

            pass

