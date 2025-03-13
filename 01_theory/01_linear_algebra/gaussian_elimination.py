from sympy import symbols, Eq, Matrix, solve, sympify
import numpy as np


def string_to_augmented_matrix(equations):
    """
    Converts a system of linear equations represented as a string into an augmented matrix.

    The function takes a string of linear equations, where each equation is separated by a newline character.
    It extracts the coefficients of the variables and the constants, and returns the augmented matrix in the form of
    variable symbols, the coefficient matrix (A), and the constant matrix (B).

    Parameters:
    -----------
    equations : str
        A string containing the system of linear equations. Each equation should be on a new line.
        Example: "2x + 3y = 5\n4x - y = 6"

    Returns:
    --------
    tuple
        A tuple containing three elements:
        1. A string of space-separated variable symbols (e.g., "x y z").
        2. A 2D NumPy array representing the coefficient matrix (A).
        3. A 2D NumPy array representing the constant matrix (B).

    Example:
    --------
    >>> equations = "2x + 3y = 5\\n4x - y = 6"
    >>> variables, A, B = string_to_augmented_matrix(equations)
    >>> print(variables)
    "x y"
    >>> print(A)
    [[ 2.  3.]
     [ 4. -1.]]
    >>> print(B)
    [[5.]
     [6.]]

    Notes:
    ------
    - The function assumes that the equations are linear and properly formatted.
    - The variables in the equations must be single lowercase letters (e.g., x, y, z).
    - The function uses SymPy's `symbols` and `sympify` to parse the equations and extract coefficients.
    - The augmented matrix is split into the coefficient matrix (A) and the constant matrix (B) for convenience.
    """

    # Split the input string into individual equations
    equation_list = equations.split("\n")
    equation_list = [x for x in equation_list if x != ""]
    # Create a list to store the coefficients and constants
    coefficients = []

    ss = ""
    for c in equations:
        if c in "abcdefghijklmnopqrstuvwxyz":
            if c not in ss:
                ss += c + " "
    ss = ss[:-1]

    # Create symbols for variables x, y, z, etc.
    variables = symbols(ss)
    # Parse each equation and extract coefficients and constants
    for equation in equation_list:
        # Remove spaces and split into left and right sides
        sides = equation.replace(" ", "").split("=")

        # Parse the left side using SymPy's parser
        left_side = sympify(sides[0])

        # Extract coefficients for variables
        coefficients.append([left_side.coeff(variable) for variable in variables])

        # Append the constant term
        coefficients[-1].append(int(sides[1]))

    # Create a matrix from the coefficients
    augmented_matrix = Matrix(coefficients)
    augmented_matrix = np.array(augmented_matrix).astype("float64")

    A, B = augmented_matrix[:, :-1], augmented_matrix[:, -1].reshape(-1, 1)

    return ss, A, B, augmented_matrix


def swap_rows(M, row_index_1, row_index_2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.
    """

    # Copy matrix M so the changes do not affect the original matrix.
    M = M.copy()
    # Swap indexes
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M


def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
    int: The index of the first non-zero value in the specified column, starting from the given row.
                Returns -1 if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:, column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array.
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol=1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return -1.
    return -1


def get_index_first_non_zero_value_from_row(M, row, augmented=False):
    """
    Find the index of the first non-zero value in the specified row of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - row (int): The index of the row to search.
    - augmented (bool): Pass this True if you are dealing with an augmented matrix,
                        so it will ignore the constant values (the last column in the augmented matrix).

    Returns:
    int: The index of the first non-zero value in the specified row.
                Returns -1 if no non-zero value is found.
    """

    # Create a copy to avoid modifying the original matrix
    M = M.copy()

    # If it is an augmented matrix, then ignore the constant values
    if augmented == True:
        # Isolating the coefficient matrix (removing the constant terms)
        M = M[:, :-1]

    # Get the desired row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns -1.
        if not np.isclose(val, 0, atol=1e-5):
            return i
    return -1


def augmented_matrix(A, B):
    """
    Create an augmented matrix by horizontally stacking two matrices A and B.

    Parameters:
    - A (numpy.array): First matrix.
    - B (numpy.array): Second matrix.

    Returns:
    - numpy.array: Augmented matrix obtained by horizontally stacking A and B.
    """
    augmented_M = np.hstack((A, B))
    return augmented_M


def row_echelon_form(A, B):
    """
    Utilizes elementary row operations to transform a given set of matrices,
    which represent the coefficients and constant terms of a linear system, into row echelon form.

    Parameters:
    - A (numpy.array): The input square matrix of coefficients.
    - B (numpy.array): The input column matrix of constant terms

    Returns:
    numpy.array: A new augmented matrix in row echelon form with pivots as 1.
    """

    # Check if matrix A (coefficient matrix) has non-zero determinant.
    det_A = np.linalg.det(A)

    # Returns "Singular system" if determinant is zero
    if np.isclose(det_A, 0):
        return "Singular system"

    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()

    # Convert matrices to float to prevent integer division
    A = A.astype("float64")
    B = B.astype("float64")

    # Number of rows in the coefficient matrix
    num_rows = len(A)

    # Transform matrices A and B into the augmented matrix M
    M = augmented_matrix(A, B)

    # Iterate over the rows.
    for row in range(num_rows):
        # Find the pivot candidate (it's always on the main diagonal)
        pivot_candidate = M[row, row]

        # If pivot_candiate is not zero, we declare it as the pivot for this row.
        if not np.isclose(pivot_candidate, 0):
            pivot = pivot_candidate
        # If pivot_candidate is zero, it cannot be a pivot. In this case we can swap with another row, which is below the current row and its element for the same column is not zero.
        else:
            first_non_zero_value_below_pivot_candidate = (
                get_index_first_non_zero_value_from_column(M, row, row)
            )
            M = swap_rows(M, row, first_non_zero_value_below_pivot_candidate)
            pivot = M[row, row]

        # Now let's divide the current row by the pivot, so the new pivot will be 1.
        M[row] = 1 / pivot * M[row]

        # Perform row reduction for rows below the current row
        for j in range(row + 1, num_rows):
            value_below_pivot = M[j, row]
            M[j] = M[j] - value_below_pivot * M[row]

    return M


def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.

    Parameters:
    - M (numpy.array): The augmented matrix in row echelon form with unitary pivots (n x n+1).

    Returns:
    numpy.array: The solution vector of the linear system.
    """

    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()

    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = M.shape[0]

    # Iterate from bottom to top
    for row in reversed(range(num_rows)):
        substitution_row = M[row]

        # Get the index of the first non-zero element in the substitution row.
        index = get_index_first_non_zero_value_from_row(M, row, augmented=True)

        # Iterate over the rows above the substitution_row
        for j in range(row):
            # Get the row to be reduced.
            row_to_reduce = M[j]

            # Get the value of the element at the found index in the row to reduce
            value = row_to_reduce[index]

            # Perform the back substitution
            row_to_reduce = row_to_reduce - value * substitution_row

            # Replace the updated row in the matrix
            M[j, :] = row_to_reduce

    # Extract the solution from the last column
    solution = M[:, -1]

    return solution


def gaussian_elimination(A, B):
    """
    Solve a linear system represented by an augmented matrix using the Gaussian elimination method.

    Parameters:
    - A (numpy.array): Square matrix of size n x n representing the coefficients of the linear system
    - B (numpy.array): Column matrix of size 1 x n representing the constant terms.

    Returns:
    numpy.array: The solution vector.
    """
    # Returns "Matrix not square" if that's the case
    if A.shape[0] != A.shape[1]:
        return "Not a square matrix"

    # Get the matrix in row echelon form
    row_echelon_M = row_echelon_form(A, B)

    if isinstance(row_echelon_M, str):
        return row_echelon_M

    # Since the system is non-singular, perform back substitution to get the result.
    solution = back_substitution(row_echelon_M)

    return solution


equations = """
2*x + 6*y + 8*z = 1
2*x + 6*y + 3*z = 1
4*y - 5*y + 8*z = 8
"""

variables, A, B, M = string_to_augmented_matrix(equations)

sols = gaussian_elimination(A, B)

if not isinstance(sols, str):
    for variable, solution in zip(variables.split(" "), sols):
        print(f"{variable} = {solution:.4f}")
else:
    print(sols)
