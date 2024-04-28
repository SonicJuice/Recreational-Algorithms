import numpy as np
import math

def atkin(limit):
    """ 1a). all numbers are deemed composites, being sieved in three layers: """
    sieve = np.zeros(limit + 1, dtype=bool)
    upper_bound = math.isqrt(limit) + 1

    """ np.arange() returns an array with evenly spaced elements as per the 
    interval. """
    x = np.arange(1, upper_bound)
    x_squared = x * x
    y_squared = np.arange(1, upper_bound) ** 2

    """ np.array() creates an ndarray which supports vectorisation (operating on 
    a set of values at once) and broadcasting (matching dimensions with 
    differently shaped arrays). """
    set_1 = np.array([1, 13, 17, 29, 37, 41, 49, 53])
    set_2 = np.array([7, 19, 31, 43])
    set_3 = np.array([11, 23, 47, 59])

    """ np.add() performes element-wise addition on two arrays; np.outer() 
    returns the outer product of two vectors. """
    n_values_1 = np.add.outer(x_squared, y_squared)
    """ np.isin() returns a boolean array indicating whether each element of an 
    array is present in another. """
    n_values_1 = n_values_1[(n_values_1 <= limit) & np.isin(n_values_1 % 60, set_1)]
    """ 1b). if n = 4x^2 + y^2 is odd and n % 60 = 1, 13, 17, 29, 37, 41, 
    49, or 53. Therefore, numbers are only prime if the quadratic has an odd 
    number of solutions and if they are square-free (not divisible by any perfect 
    square besides 1). """
    sieve[n_values_1] = ~sieve[n_values_1]

    n_values_2 = np.add.outer(3 * x_squared, y_squared)
    n_values_2 = n_values_2[(n_values_2 <= limit) & np.isin(n_values_2 % 60, set_2)]
    """ 1c). if n = 3x^2 + y^2 is odd and n % 60 = 7, 19, 31, or 43. """
    sieve[n_values_2] = ~sieve[n_values_2]

    """ y_greater_x indicates, for each combination of elements from 
    y_squared and x_squared, whether an element in y_squared > than the 
    corresponding element in x_squared. """
    y_greater_x = y_squared[:, None] > x_squared
    """ np.where() returns the indices of condition-satisfying elements. """
    n_values_3 = np.where(y_greater_x, 3 * x_squared[:, None] - y_squared, 0)
    n_values_3 = n_values_3[(n_values_3 <= limit) & np.isin(n_values_3 % 60, set_3)]
    """ 1d). if n = 3x^2 - y^2 is odd and n % 60 = 11, 23, 47 or 59. """
    sieve[n_values_3] = ~sieve[n_values_3]

    """ mark multiples of squares as composite. """
    n = np.arange(5, upper_bound, 2)
    sieve[n ** 2] = False
    for prime in n:
        if sieve[prime]:
            sieve[prime * prime :: prime] = False

    """ np.flatnonzero() returns non-zero indices in a copied array collapsed 
    into one dimension. Time complexity: O(n / log log n), which is < 
    Eratosthenes as more composites are sieved in fewer iterations. """
    return np.r_[2, 3, 5, np.flatnonzero(sieve)[:len(np.flatnonzero(sieve[sieve < limit]))]]
