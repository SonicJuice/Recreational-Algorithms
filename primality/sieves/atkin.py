import numpy as np
import math

def atkin(limit):
    """ all numbers within the limit are deemed composites, which are sieved in 
    three layers: """
    sieve = np.zeros(limit + 1, dtype=bool)
    upper_bound = math.isqrt(limit) + 1
    x_squared = [x * x for x in range(1, upper_bound)]
    y_squared = [y * y for y in range(1, upper_bound)]
    set_1 = {1, 13, 17, 29, 37, 41, 49, 53}
    set_2 = {7, 19, 31, 43}
    set_3 = {11, 23, 47, 59}

    for x_sq in x_squared:
        for y_sq in y_squared:

            """ a). if n = 4x^2 + y^2 is odd and n % 60 = 1, 13, 17, 29, 37, 41, 
            49, or 53). Therefore, these numbers are only prime if the quadratic 
            has an odd number of solutions and if they are square-free (not 
            divisible by any perfect square besides 1). """
            n = 4 * x_sq + y_sq
            if n <= limit and n % 60 in set_1:
                sieve[n] = not sieve[n]

            """ b). if n = 3x^2 + y^2 is odd and n % 60 = 7, 11, 19, 31, or 37 """
            n = 3 * x_sq + y_sq
            if n <= limit and n % 60 in set_2:
                sieve[n] = not sieve[n]

            """ c). if n = 3x^2 - y^2 is odd and n % 60 = 11, 23, 47 or 59. """
            if x_sq > y_sq:
                n = 3 * x_sq - y_sq
                if n <= limit and n % 60 in set_3:
                    sieve[n] = not sieve[n]

    """ mark multiples of squares as non-prime. """    
    for n in range(5, upper_bound, 2):
        if sieve[n]:
            n_sq = n * n
            sieve[n_sq::n_sq] = False

    """ np.flatnonzero() returns non-zero indices in a copied array collapsed 
    into one dimension. Time complexity: O(n / log log n), which is < 
    Eratosthenes as more composites are sieved in fewer iterations. """
    return np.r_[2, 3, 5, np.flatnonzero(sieve)]
