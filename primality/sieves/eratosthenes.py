import math
import numpy as np

def eratosthenes(n):
    """ reaching the square root of n, where n is the upper limit of the range being 
    sieved, means that all the composites have already been marked. """
    upper_bound = math.isqrt(n) + 1
    """ np.ones() returns a new array of the given data type 
    with values of 1 to track primality. """
    primes = np.ones(n + 1, dtype=bool)
    """ even numbers are marked as composite by moving with a step of 2 from index 4; 
    multiples of 3 also are, being marked via a step of 6 from index 9. """
    primes[:2] = primes[4::2] = primes[9::6] = False

    """ all primes excluding 2 and 3 can be written in the form 6k +/- 1; thus, iterate 
    through and mark all numbers in these forms. """
    for i in range(5, math.isqrt(upper_bound), 6):
        if primes[i]:
            primes[i * i :: 2 * i] = False

    for j in range(7, upper_bound, 6):
        """ only mark odd multiples; start from i * i since all multiples < this would
        have already been marked as composite, and move in steps of 2i to skip even 
        multiples, which are already marked as composite). """
        if primes[j]:
            primes[j * j :: 2 * j] = False

    """ np.nonzero() returns the indices of condition-satisfying elements; time complexity: 
    'O(n log log n)'"""
    return np.where(primes)[0]
