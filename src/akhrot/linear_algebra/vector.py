from typing import List

Vector = List[float]

def add(v:Vector, w:Vector) -> Vector:
    "Adds two vectors and returns the resultant vector"
    assert len(v) == len(w), "Vectors of different length can't be added"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v:Vector, w:Vector) -> Vector:
    "Substract vector w from vector v and returns the resultant vector"
    assert len(v) == len(w), "Vectors of different length can't be added"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "No vectors to add"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "All vectors are not same size"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c:float, v:Vector) -> Vector:
    return [c*v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    v_len = len(vectors)
    assert v_len != 0, "No vectors provided"
    return scalar_multiply(1/v_len, vector_sum(vectors))

def dot_product(v:Vector, w:Vector) -> float:
    "dot_product([v, w]) => ∑ v_i*w_i"
    assert len(v) == len(w), "length of vectors must be same"
    return sum(v_i*w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v:Vector) -> float:
    "sum_of_squares(v) => ∑v_i*v_i"
    return dot_product(v, v)

def magnitude(v:Vector) -> float:
    return sum_of_squares(v) ** 0.5

def squared_distance(v:Vector, w:Vector) -> float:
    "squared_distance(v,w) => ∑(v_i-w_i)^2"
    return sum_of_squares(substract(v, w))

def distance(v:Vector, w:Vector) -> float:
    return squared_distance(v, w) ** 0.5

def _test():
    assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
    assert scalar_multiply(2, [1, 2]) == [2, 4]
    assert vector_mean([[1,2,3], [4,5,6], [7,8,9]]) == [4, 5, 6]
    assert dot_product([1, 2], [3, 4]) == 11

if __name__ == '__main__':
    _test()
