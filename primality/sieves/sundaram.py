import numpy as np
import math

def sundaram(n):
    """ only focus on odd numbers. """
    limit = (n - 1) // 2
    """ upon exceeding isqrt(limit), (i + j + 2 * i * j) becomes > limit. Thus, 
    iterating up to isqrt(limit) ensures all possible combinations of (i, j) are 
    covered non-redundantly. 
    """
    primes = np.ones(limit, dtype=bool)

    for i in range(1, math.isqrt(limit) + 1):
        if primes[i]:
            """
            an integer q of the form 2x + 1 is only excluded if x is of the form 
            i + j + 2ij. That means: q = 2(i + j + 2ij) + 1 = (2i + 1)(2j + 1).
            Thus, an odd integer is only excluded if it has the above 
            form of factorization (i.e. a non-trivial odd factor). 
            """
            primes[2 * i * (i + 1) :: (2 * i + 1)] = False

    """ as the array only represents odds, compute the corresponding primes by 
    doubling and adding one to the indices; time complexity: O(n log n) """
    return np.r_[2, 2 * np.nonzero(primes)[0][1:] + 1]
