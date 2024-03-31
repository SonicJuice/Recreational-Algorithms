from math import isqrt
import numpy as np

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return
    """ represents the number of odds <= 'limit'. """
    size = (limit - 1) // 2
    """ 'np.ones()' returns a new array of the given shape and data type, with values of '1', to track primality. """
    prime = np.ones(size + 1, dtype=bool)
    """ '.isqrt()' gets the integer square root of the given non-negative integer 'n'. It returns the floor value of the exact sqrt 
    of 'n', or equivalently the greatest integer 'a' such that 'a^2 <= n'. """
    for i in range(1, isqrt(limit) // 2 + 1):
        if prime[i]:
            p = i * 2 + 1
            """ updates all elements of 'prime' that correspond to multiples of the current prime 'p'. """
            prime[i + p::p] = False
    """ 'np.concatenate()' joins two or more arrays along an axes (row and column); '.nonzero()' computes the indices of non-zero elements, 
    returning a tuple of arrays for each axes."""
    primes = np.concatenate(([2], np.nonzero(prime)[0] * 2 + 1))
    return primes

if __name__ == '__main__':
    """ time complexity: 'O(n log log n)' """
    sieveOfEratosthenes(10 ** 8)
