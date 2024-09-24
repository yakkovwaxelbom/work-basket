from typing import List


def extract_solution(memoized, matrices, i, j):
    """
    Extract the optimal order of matrix multiplication.

    This function recursively determines the optimal placement of parentheses in the matrix chain multiplication.

    Parameters:
    - memoized (List[List[int]]): The DP table holding the minimum multiplication cost for each subproblem.
    - matrices (List[List[int]]): The list of matrices.
    - i (int): The start index of the subchain.
    - j (int): The end index of the subchain.

    Returns:
    - str: A string representation of the optimal multiplication order with parentheses.
    """
    if i == j:
        return f"M{i + 1}"

    for k in range(i, j):
        cost = memoized[i][k] + memoized[k + 1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
        if cost == memoized[i][j]:
            left_part = extract_solution(memoized, matrices, i, k)
            right_part = extract_solution(memoized, matrices, k + 1, j)
            return f"({left_part} x {right_part})"


def Matrix_chain_multiplication(matrices: List[List[float]]) -> str:
    """
    Matrix Chain Multiplication Problem:

    The goal is to find the most efficient way to multiply a given sequence of matrices. The order in which
    the matrices are multiplied affects the number of operations. We need to determine the minimum number of
    scalar multiplications required to multiply the entire chain of matrices.

    ### Problem Description:
    Given a sequence of matrices, we want to find the optimal way to parenthesize the matrix multiplication
    such that the total number of scalar multiplications is minimized.

    The matrix multiplication is associative, meaning that given matrices A, B, and C:
    - (AB)C = A(BC)

    However, the number of operations may vary depending on how we choose to perform the multiplication.

    ### Approach:
    This problem is solved using dynamic programming (DP). We define `dp[i][j]` as the minimum number of
    scalar multiplications required to compute the product of matrices from `i` to `j`.

    The recurrence relation is:
    ```
    dp[i][j] = min(dp[i][k] + dp[k+1][j] + cost of multiplying matrices A_i to A_k with A_(k+1) to A_j)
    for all k, where i <= k < j
    ```

    ### Parameters:
    - `matrices (List[List[float]])`: A list of matrices represented by their dimensions. Each matrix is
      represented as a list where the first number is the number of rows and the second number is the number
      of columns.

    ### Returns:
    - `List[List[int]]`: The minimum number of scalar multiplications required to multiply the chain of matrices.

    ### Example:
    ```
    Input: [[10, 30], [30, 5], [5, 60]]
    Output: Optimal order of multiplication: ((M1 x M2) x M3)

    ```
    Explanation: The optimal parenthesization minimizes the number of scalar multiplications.
    """

    # Extract the dimensions of the matrices
    n = len(matrices)
    p = [matrices[0][0]] + [matrices[i][1] for i in range(n)]
    print(p)

    # Initialize the memoized table
    memoized = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the memoized table
    for length in range(2, n + 1):  # length of the chain
        for i in range(n - length + 1):
            j = i + length - 1
            memoized[i][j] = float('inf')
            for k in range(i, j):
                cost = memoized[i][k] + memoized[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < memoized[i][j]:
                    memoized[i][j] = cost

    # Return the minimum cost for multiplying the full chain
    return extract_solution(memoized, matrices, 0, len(matrices) - 1)


matrices = [[10, 30], [30, 5], [5, 60], [5,60], [5,60]]

print("Optimal order of multiplication:", Matrix_chain_multiplication(matrices))
