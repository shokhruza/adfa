import numpy as np


def gaussian_elimination(A, b):
    n = len(b)
    # Augmented matrix
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)

    # Forward elimination
    for i in range(n):
        # Partial pivoting
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]

        pivot = Ab[i, i]
        Ab[i] /= pivot
        for j in range(i + 1, n):
            factor = Ab[j, i]
            Ab[j] -= factor * Ab[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, :-1], x)

    return x


# Example usage
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

solution = gaussian_elimination(A, b)
print("Solution:", solution)
