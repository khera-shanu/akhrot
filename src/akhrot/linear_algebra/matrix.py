from typing import List, Tuple, Callable
from .vector import Vector

Matrix = List[Vector]

def shape(A:Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A:Matrix, i:int) -> Vector:
    return A[i]

def get_column(A:Matrix, j:int) -> Vector:
    return [A_i[j] for A_i in A]

def make_matrix(num_rows:int, num_cols:int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n:int) -> Matrix:
    return make_matrix(n, n, lambda i,j: 1 if i==j else 0)

def _test():
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
    assert get_row([[1, 2, 3], [4, 5, 6]], 1) == [4, 5, 6]
    assert get_column([[1, 2, 3], [4, 5, 6]], 1) == [2, 5]
    assert identity_matrix(3) == [
                                    [1, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 1]
                                 ]
