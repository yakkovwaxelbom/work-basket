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


# Example usage
if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = recession_matrix_multiplication(matrix1, matrix2)
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
