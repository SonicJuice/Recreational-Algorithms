from math import sqrt
def is_prime(n):
    """ all primes > 3 are writable as '6k + 1' or '6k - 1', where 'k' is a positive integer. """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    """ only need to check if 'n' is divisible by primes of the aforementioned forms up to 'sqrt(n)'. """
    while i <= int(sqrt(n)):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    """ time complexity: 'O(sqrt(n))' """
    print(is_prime())
