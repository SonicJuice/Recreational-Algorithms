import math
import numpy as np

def eratosthenes(limit):
    if limit < 2:
        return
    """ np.ones() returns a new array of the given data type 
    with values of 1 to track primality. """  
    size = (limit) // 2
    numbers = np.ones(size, dtype=bool)
    numbers[:2] = False
    sqrt_limit = math.isqrt(limit)
    """ math.isqrt() returns the integer square root of the given non-negative 
    integer This is the floor value of the exact square root of n (i.e the greatest 
    integer a such that a^2 <= n. """
    for i in range(2, sqrt_limit):
        if numbers[i]:
            numbers[i*i:limit:i] = False
    """ np.nonzero() returns the indices of non-zero elements. """
    primes = np.nonzero(numbers)[0]
    return primes.tolist()
