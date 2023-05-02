import numpy as np
import time

def sieveOfAtkin(limit):
    if limit < 2:
        return []

    sieve = np.zeros(limit + 1, dtype=bool)
    primes = [2, 3]
    sqrt_limit = int(np.sqrt(limit)) + 1

    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for n in range(5, sqrt_limit):
        if sieve[n]:
            primes.append(n)
            sieve[n**2::n**2] = False

    for n in range(sqrt_limit, limit+1):
        if sieve[n]:
            primes.append(n)

    return primes

def nthPrime(n):
    primes = sieveOfAtkin(10 ** 6)
    if n > len(primes):
        return None
    return primes[n - 1]

if __name__ == '__main__':
    start = time.time()
    print(nthPrime(10001))
    print(time.time() - start)
