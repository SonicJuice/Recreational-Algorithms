import numpy as np
import math

def eratosthenes(n):
    """ np.ones() returns a new array of the given data type 
    with values of 1 to track primality. """
    primes = np.ones(n, dtype=bool)
    """ reaching isqrt(n) means all composites have already been marked. """
    upper_bound = math.isqrt(len(primes)) + 1
    """ even numbers are marked as composite by moving with a step of 2 from index 
    4; as are multiples of 3, being marked via a step of 6 from index 9. """
    primes[:2] = primes[4::2] = primes[9::6] = False

    """ all primes besides 2 and 3 can be written as 6k +/- 1. """
    for i in range(5, upper_bound, 6):
        if primes[i]:
            primes[i * i :: 2 * i] = False

    for j in range(7, upper_bound, 6):
        if primes[j]:
            """ only mark odd multiples; start from j * j since lower multiples 
            would have already been marked as composite. Move in steps 
            of 2j to skip even multiples. """
            primes[j * j :: 2 * j] = False

    """ np.flatnonzero() returns non-zero indices in the flattened version of a; 
    time complexity: O(n log log n) """
    return np.flatnonzero(primes)
