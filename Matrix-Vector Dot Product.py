import numpy

def matrix_dot_vector(a: list[list[int | float]], 
                      b: list[int | float]) -> list[int | float]:

    # Convert to numpy arrays
    A = numpy.array(a)
    B = numpy.array(b)

    # Validate dimensions
    if A.ndim != 2 or B.ndim != 1:
        return -1
    
    # Number of columns in A must match length of B
    if A.shape[1] != B.shape[0]:
        return -1

    # Perform dot product
    result = A.dot(B)

    # Convert back to Python list
    return result.tolist()