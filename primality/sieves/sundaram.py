def sundaram(limit):
    if limit < 2:
        return  
    size = (limit - 1) // 2
    sieve = [True] * (size + 1)

    for i in range(1, size + 1):
        j = i
        """ for each pair (i, j), calculate the corresponding sieve index via i + j 
        + 2 * i * j; this represents an odd composite. """
        while i + j + 2 * i * j <= size:
            sieve[i + j + 2 * i * j] = False
            j += 1

    """ after iterating through all pairs, generate primes via sieve, then calculate 
    an odd prime (represented by True). finally, calculate this prime via 2 * i + 1;
    enumerate() returns a collection as an enumerate object, adding a counter as its
    key. """
    primes = [2] + [2 * i + 1 for i, is_prime in enumerate(sieve[1:], start = 1) if is_prime]
    """ time complexity: 'O(n log n)' """
    return primes
