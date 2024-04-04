import numpy as np
import math

def eratosthenes(limit):
    if limit < 2:
        return 
    even_limit = (limit + 1) // 2
    """ np.ones() returns a new array of the given data type 
    with values of 1 to track primality. """
    numbers = np.ones(even_limit, dtype=bool)
    numbers[0] = False 

    sqrt_limit = math.isqrt(limit)
    for i in range(1, (sqrt_limit + 1) // 2):
        if numbers[i]:
          """ math.isqrt() returns the integer square root of the given non-
          negative integer This is the floor value of the exact square root 
          of n (i.e the greatest integer a such that a^2 <= n. """
          prime = 2 * i + 1
          """ multiples of the prime as not prime. """
          numbers[prime * prime // 2: even_limit: prime] = False

    """ convert boolean array into a list of primes via the indices of non-
    zero elements """
    primes = [2] + [2 * i + 1 for i in np.nonzero(numbers)[0]]
    """ time complexity: 'O(n log log n)' """
    return primes
