def sundaram(limit):
    if limit < 2:
        return
    size = (limit - 1) // 2
    sieve = [True] * (size + 1)
    for j in range(1, size + 1):
        i = 1
        """ for each pair '(i, j)', calculate the corresponding index in 'sieve' via 'i + j + 2 * i * j'; this represents an odd 
        composite."""
        while i <= j and (i + j + 2 * i * j) <= size:
            sieve[i + j + 2 * i * j] = False
            i += 1
    """ after iterating through all pairs, generate primes via 'sieve', then calculate an odd prime (represented by 'True'). 
    Finally, calculate this prime via '2 * i + 1'; 'enumerate()' returns a collection as an enumerate object, adding a counter as its key. """
    primes = [2] + [(2 * i + 1) for i, is_prime in enumerate(sieve) if is_prime]
    """ time complexity: 'O(n log n)' """
    return primes
