from akhrot.linear_algebra.vector import Vector, dot_product, sum_of_sqaures
from collections import Counter

def mean(v: Vector) -> float:
    return sum(v)/len(v)

def _median_odd(v: Vector) -> float:
    return sorted(v)[len(v)//2]

def _median_even(v: Vector) -> float:
    sorted_v = sorted(v)
    hi_mid = sorted_v[len(v)//2]
    low_mid = sorted_v[len(v)//2 - 1]
    return (hi_mid + low_mid)/2

def median(v: Vector) -> float:
    return _median_even(v) if len(v)%2 == 0 else _median_odd(v)

def quantile(v:Vector, p:float) -> float:
    '''
    quantile represents the value under which certain value lies
    median is a special case of quantile where p=0.5
    '''
    p_index = int(p * len(v))
    return sorted(v)[p_index]

def mode(v:Vector) -> Vector:
    "returns a vector of most common values"
    counts = Counter(v)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

def de_mean(v:Vector) -> Vector:
    v_bar = mean(v)
    return [v_i - v_bar for v_i in v]

def variance(v:Vector) -> float:
    n = len(v)
    assert n >= 2, "Variance require atleast 2 values"
    deviations = de_mean(v)
    return sum_of_squares(deviations)/(n-1)

def standard_deviation(v:Vector) -> float:
    return variance(v) ** 0.5

def interquartile_range(v:Vector) -> float:
    return quantile(v, 0.25) - quantile(v, 0.75)

def covariance(v:Vector, w:Vector) -> float:
    assert len(v) == len(w), "length of both vectors must be same"
    return dot_product(de_mean(v), de_mean(w))

def correlation(v:Vector, w:Vector) -> float:
    std_x = standard_deviation(v)
    std_y = standard_deviation(w)
    if std_x > 0 and std_y > 0:
        return covariance(v, w) / (std_x * std_y)
    else: return 0

def _test():
    assert mean([1,2,3,4,5]) == 3
    assert median([1,2,3,4,5]) == 3
    assert median([1,2,3,4]) == 2.5
    assert quantile([1,2,3,4], 0.75) == 4
    assert set(mode([1,1,2,2,3,3,3,4,4,4,5])) == {3,4}
