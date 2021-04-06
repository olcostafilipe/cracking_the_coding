"""
Question 08: Zero matrix
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0
"""

import numpy as np  # just for visualization

def zero_matrix(matrix: list) -> list:
    rows_to_zero = []
    cols_to_zero = []
    
    # First pass: check rows and cols indexes to set to zero 
    for r in range (len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                rows_to_zero.append(r)
                cols_to_zero.append(c)
    
    # Second pass: update indexes to set to zero 
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r in rows_to_zero or c in cols_to_zero:
                matrix[r][c] = 0

    return matrix


def main():
    # Matrices do test
    mat_01 = np.array([[1, 1, 1, 1, 1],
                       [2, 2, 2, 2, 2],
                       [3, 3, 0, 3, 3],
                       [4, 4, 4, 4, 4],
                       [5, 5, 5, 5, 5]])

    mat_02 = np.array([[0, 2, 3, 4, 5, 6],
                       [2, 4, 6, 8, 10, 12],
                       [3, 6, 9, 12, 15, 18],
                       [4, 8, 12, 0, 20, 24],
                       [5, 10, 15, 20, 25, 30],
                       [6, 12, 18, 24, 30, 0]])

    mat_03 = np.array([[1, 2, 3, 4],
                       [2, 4, 6, 8],
                       [0, 6, 9, 12],
                       [4, 8, 12, 16],
                       [5, 10, 15, 20]])
    
    mat_04 = np.array([[7, 1, 3, 7, 2],
                       [4, 0, 9, 5, 3],
                       [6, 3, 3, 2, 8],
                       [5, 3, 6, 4, 9],
                       [7, 0, 1, 2, 5]])

    print(mat_01)
    print(zero_matrix(mat_01))
    print()
    print(mat_02)
    print(zero_matrix(mat_02))
    print()
    print(mat_03)
    print(zero_matrix(mat_03))
    print()
    print(mat_04)
    print(zero_matrix(mat_04))


if __name__ == '__main__':
    main()
