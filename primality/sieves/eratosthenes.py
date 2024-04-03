import math
import numpy as np

def eratosthenes(limit):
    if limit < 2:
        return
    """ np.ones() returns a new array of the given data type 
    with values of 1 to track primality. """  
    numbers = np.ones(limit - 1, dtype=bool)

    """ math.isqrt() returns the integer square root of the given non-negative 
    integer This is the floor value of the exact square root of n (i.e the greatest 
    integer a such that a^2 <= n. """
    for i in range(2, math.isqrt(limit) + 1):
        if numbers[i-2]:
            numbers[i*i-2:limit-1:i] = False
    """
    np.nonzero() returns the indices of non-zero elements.
    """
    primes = np.nonzero(numbers)[0] + 2
    """ Time complexity: 'O(n log log n)' """
    return primes.tolist()
