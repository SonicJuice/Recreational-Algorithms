def sieveOfAtkin(limit):
    if limit < 2:
        return

    """ all numbers within the limit are deemed composites, which are sieved in three layers: """
    sieve = [False] * (limit + 1)
    sieve[2], sieve[3] = True, True
    sqrt_limit = int(limit ** 0.5) + 1
    squares = [i * i for i in range(1, sqrt_limit)]

    for x in range(1, sqrt_limit):
        x_square = squares[x - 1]
        for y_square in squares:
            """ a) 'n = (4 * x * x) + (y * y)' has an odd no. of solutions (i.e., there's an odd number of distinct pairs '(x, y)' that satisfy 
            'and n % 12 = 1 or n % 12 = 5'). """
            n = 4 * x_square + y_square
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            """ b) 'n = (3 * x * x) + (y * y)' has an odd no. of solutions 'and n % 12 = 7'. """
            n = 3 * x_square + y_square
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            """ c) 'n = (3 * x * x) - (y * y)' has an odd no. of solutions 'if x > y ** 0.5 and n % 12 = 11'. """
            if x > y_square ** 0.5:
                n = 3 * x_square - y_square
                if n <= limit and n % 12 == 11:
                    sieve[n] = not sieve[n]

    """ 'yield' returns a generator object to the function caller, rather than a value. """
    yield 2
    yield 3

    """ mark all mulitples of squares as non-prime. """
    for n in range(5, limit + 1):
        if sieve[n]:
            yield n
            for k in range(n * n, limit + 1, 2 * n * n):
                sieve[k] = False

if __name__ == '__main__':
    sieveOfAtkin(10 ** 8)

""" time complexity: 'O(n / log log n)'; traditionally faster than SOE as more composites are sieved in fewer iterations. """
