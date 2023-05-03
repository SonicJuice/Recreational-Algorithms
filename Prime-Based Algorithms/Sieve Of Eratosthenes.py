from math import isqrt
import numpy as np

def sieveOfEratosthenes(limit):
    if limit < 2:
        return []

    """ represents the number of odds <= 'limit'. """
    size = (limit - 1) // 2
    """ 'np.ones()' returns a new array of the given shape and data type, with values of '1'; acts as a primality tracker. """
    prime = np.ones(size + 1, dtype=bool)

    """ '.isqrt()' gets the integer square root of the given non-negative integer 'n'. It returns the floor value of the exact sqrt of 'n', or equivalently the greatest integer 'a' such that 'a^2 <= n'. """
    for i in range(1, isqrt(limit) // 2 + 1):
        if prime[i]:
            p = i * 2 + 1
            """ updates all elements of 'prime' that correspond to multiples of the current prime 'p'. """
            prime[i + p::p] = False
          
    """ '.concatenate()' joins two or more arrays along a specified axis; '.arrange()' returns evenly spaced values within a 
    given interval (in the case of three arguments, values are generated within the half-open interval, with spacing between values given by step). """
    primes = np.concatenate(([2], np.arange(3, limit, 2)[prime[1:]]))

    return primes

if __name__ == '__main__':
    sieveOfEratosthenes(10 ** 8)

""" time complexity: 'O(n log log n)' """
