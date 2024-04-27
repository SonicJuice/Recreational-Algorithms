import numpy as np
import math

def eratosthenes(n):
    """ np.ones() returns a new array of the given data type 
    with values of 1 to track primality. For every three numbers, two 
    aren't divisible by 3. (n % 6 == 2) accounts for when n isn't 
    divisible by 6 and, thus, might include an additional prime."""
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
  
    """ reaching isqrt(len(sieve)) means all composites have already been 
    marked; // 3 only accounts for odds """
    for i in range(1, math.isqrt(len(sieve)) + 1 // 3):
        if sieve[i]:
            """ formula for the current prime; bitwise OR with 1 ensures 
            this is always odd. """
            k = 3 * i + 1 | 1
            """ mark multiples of k (starting from k^2) as composite. """
            sieve[k * k // 3 :: 2 * k] = False
            """ if i is even, (i & 1) equals 0, simplifying the expression to k * 
            (k + 4) // 3, marking multiples congruent to 1 mod 6. If i is odd, (i 
            & 1) equals 1, simplifying the expression to k * (k + 2) // 3, 
            marking multiples congruent to 5 mod 6 """
            sieve[k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = False
    """ np.r_ concatenates array slices along row (first) 
    axis. np.nonzero() returns the indices of non-zero array elements; 
    time complexity: O(n log log n) """
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]
