import math

def atkin(limit):
    """ all numbers within the limit are deemed composites, which are sieved in 
    three layers: """
    sieve = [False] * (limit + 1)
    primes = [2, 3]
    sqrt_limit = math.isqrt(limit) + 1
  
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            x_square = x * x
            y_square = y * y
  
            """ a) n = (4 * x * x) + (y * y) has an odd no. of solutions (i.e. an odd
            number of distinct pairs '(x, y)) that satisfy and n % 12 = 1 or 
            n % 12 = 5. """
            n = 4 * x_square + y_square
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
  
            """ b) n = (3 * x * x) + (y * y) has an odd no. of solutions 
            that satifsy and n % 12 = 7. """
            n = 3 * x_square + y_square
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
  
            """ c) n = (3 * x * x) - (y * y) has an odd no. of solutions that 
            satisfy if x > y ** 0.5 and n % 12 = 11. """
            if x > y:
                n = 3 * x_square - y_square
                if n <= limit and n % 12 == 11:
                    sieve[n] = not sieve[n]
  
    """ mark all multiples of squares as non-prime. """    
    for n in range(5, sqrt_limit, 2):
        if sieve[n]:
            n_square = n * n
            for k in range(n_square, limit + 1, n_square):
                sieve[k] = False
  
    """ append sieved primes. """
    for n in range(5, limit + 1, 2):
        if sieve[n]:
            primes.append(n)
  
    """ time complexity: 'O(n / log log n)'; traditionally faster than Eratosthenes
    as more composites are sieved in fewer iterations. """
    return primes
