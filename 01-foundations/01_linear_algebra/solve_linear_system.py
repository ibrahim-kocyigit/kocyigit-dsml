import numpy as np


def solve_linear_system(matrix, vector):
    """
    Solves the linear system Ax = b and returns the solution vector x.

    Args:
        matrix (np.ndarray): Coefficient matrix A.
        vector (np.ndarray): Constant vector b.

    Returns:
        np.ndarray: Solution vector x.

    Raises:
        ValueError: If the matrix is singular, dimensions are mismatched, or input is invalid.
        LinAlgError: If the matrix is not square.
    """
    # Validate input types
    if not (isinstance(matrix, np.ndarray) and isinstance(vector, np.ndarray)):
        raise ValueError("Inputs must be NumPy arrays.")

    # Ensure matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Coefficient matrix must be square.")

    # Ensure dimensions of A and b are compatible
    if matrix.shape[0] != vector.shape[0]:
        raise ValueError(
            "Dimension mismatch: The number of rows in A must match the length of b."
        )

    # Check if the matrix is singular
    determinant = np.linalg.det(matrix)
    if np.isclose(determinant, 0):
        raise ValueError("Error: Singular matrix (determinant is zero).")

    # Check for ill-conditioned matrix
    condition_number = np.linalg.cond(matrix)
    if condition_number > 1e10:  # Threshold for ill-conditioned matrix
        print(
            f"Warning: Matrix is ill-conditioned (condition number = {condition_number:.2e})."
        )

    # Solve the linear system
    solution = np.linalg.solve(matrix, vector)
    return solution


def main():
    # Define the coefficient matrix A and constant vector b
    A = np.array([[4, -3, 1], [2, 1, 3], [-1, 2, -5]], dtype=float)

    b = np.array([-10, 0, 17], dtype=float)

    try:
        # Solve the linear system
        solution = solve_linear_system(A, b)
        print("Solution vector x:", solution)
    except (ValueError, np.linalg.LinAlgError) as e:
        print(e)


if __name__ == "__main__":
    main()
