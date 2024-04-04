import math
import numpy as np

def eratosthenes(n):
  """ limit accounts for odd numbers only, as no primes except 2 are even """
  limit = math.isqrt((n - 1) // 2) + 1
  """ np.ones() returns a new array of the given data type 
  with values of 1 to track primality. """
  primes = np.ones(n + 1, dtype=bool)
  """ mark multiples of 2 and 3 as not prime, starting from indices 4 and 9, 
  respectively, in steps of 2 and 6 """
  primes[:2] = primes[4::2] = primes[9::6] = False
  for i in range(5, limit, 6):
      if primes[i]:
          primes[i * i :: 2 * i] = False

  """ all primes excluding 2 and 3 can be written in the form 6k +/- 1 """
  for j in range(7, limit, 6):
      if primes[j]:
          """ mark multiples of prime as non-prime """
          primes[j * j :: 2 * j] = False
        
  """ np.nonzero() returns the indices of the non-zero values """
  return np.flatnonzero(primes)
