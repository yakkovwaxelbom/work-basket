import copy

import numpy as np


def split_matrix(matrix):
    """Split a matrix into four sub-matrices."""
    size = len(matrix)
    half = size // 2
    a = [row[:half] for row in matrix[:half]]
    b = [row[half:] for row in matrix[:half]]
    c = [row[:half] for row in matrix[half:]]
    d = [row[half:] for row in matrix[half:]]
    return a, b, c, d


def add_matrices(matrix1, matrix2):
    """Add two matrices."""
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def subtract_matrices(matrix1, matrix2):
    """Subtract two matrices."""
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


def recession_matrix_multiplication(matrix1, matrix2):
    """Multiply two matrices using the Strassen algorithm."""
    size = len(matrix1)

    if size == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    # Split the matrices into sub-matrices
    a, b, c, d = split_matrix(matrix1)
    e, f, g, h = split_matrix(matrix2)

    # Calculate the 7 products using Strassen's method
    p1 = recession_matrix_multiplication(a, subtract_matrices(f, h))
    p2 = recession_matrix_multiplication(add_matrices(a, b), h)
    p3 = recession_matrix_multiplication(add_matrices(c, d), e)
    p4 = recession_matrix_multiplication(d, subtract_matrices(g, e))
    p5 = recession_matrix_multiplication(add_matrices(a, d), add_matrices(e, h))
    p6 = recession_matrix_multiplication(subtract_matrices(b, d), add_matrices(g, h))
    p7 = recession_matrix_multiplication(subtract_matrices(a, c), add_matrices(e, f))

    # Combine the results into one matrix
    quadrant1 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    quadrant2 = add_matrices(p1, p2)
    quadrant3 = add_matrices(p3, p4)
    quadrant4 = add_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)

    # Combine the quadrants into a single matrix
    top_half = [quadrant1[i] + quadrant2[i] for i in range(len(quadrant1))]
    bottom_half = [quadrant3[i] + quadrant4[i] for i in range(len(quadrant3))]
    result = top_half + bottom_half

    return result


def transpose_matrix(matrix: list) -> np.ndarray:
    # Create an empty matrix with the dimensions swapped
    solution = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    # Fill the transposed matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            solution[j][i] = matrix[i][j]

    # Convert the result to a NumPy array and return
    return np.array(solution)


def matching_rows(matrix: list, i: int) -> list:
    if matrix[i][i] == 0:
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                matrix[i], matrix[j] = matrix[j], matrix[i]
                return matrix
    return matrix


def ranking_matrices(matrix: list) -> list:
    # Step down
    for i in range(len(matrix)):
        matrix = matching_rows(matrix, i)
        if matrix[i][i] == 0:
            break
        x = 1 / matrix[i][i]
        for j in range(len(matrix[0]) - i):
            matrix[i][j + i] *= x
        for k in range(i + 1, len(matrix)):
            x = matrix[k][i]
            for l in range(len(matrix[0])):
                matrix[k][l] -= x * matrix[i][l]
    # Step up
    for i in range(len(matrix) - 1, 0, -1):
        if matrix[i][i] != 0 and matrix[i - 1][i] != 0:
            for j in range(i - 1, -1, -1):
                x = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix[0]) - 1, i - 1, -1):
                    matrix[j][k] -= x * matrix[i][k]
    return matrix


def create_identity_matrix(size: int) -> list:
    matrix = [[0 for item in range(size)] for row in range(size)]
    for i in range(size):
        matrix[i][i] = 1
    return matrix


def create_invertible_matrix(matrix_1: list) -> list[list]:
    matrix = copy.deepcopy(matrix_1)
    if len(matrix) == len(matrix[0]):
        invertible_matrix = create_identity_matrix(len(matrix))
        for i in range(len(matrix)):
            matrix = matching_rows(matrix, i)
            if matrix[i][i] == 0:
                break
            x = 1 / matrix[i][i]
            for j in range(len(matrix[0])):
                matrix[i][j] *= x
                invertible_matrix[i][j] *= x
            for k in range(i + 1, len(matrix)):
                x = matrix[k][i]
                for l in range(len(matrix[0])):
                    matrix[k][l] -= x * matrix[i][l]
                    invertible_matrix[k][l] -= x * invertible_matrix[i][l]
        for i in range(len(matrix)):
            if matrix[i][i] == 0:
                raise ValueError("The matrix has a linear dependence and is therefore not invertible")
        for i in range(len(matrix) - 1, 0, -1):
            if matrix[i][i] != 0 and matrix[i - 1][i] != 0:
                for j in range(i - 1, -1, -1):
                    x = matrix[j][i] / matrix[i][i]
                    for k in range(len(matrix[0]) - 1, - 1, -1):
                        matrix[j][k] -= x * matrix[i][k]
                        invertible_matrix[j][k] -= x * invertible_matrix[i][k]
        return invertible_matrix
    raise ValueError("A non-square matrix and therefore not invertible")
