from random import randint

def _power(x, y, p):
    result = 1 
    x %= p # reduce 'x' if it's '>= p' to prevent overflow
    while y > 0:
        if y & 1: # determine if 'y' is odd via bitwise AND
            result = (result * x) % p
        y >>= 1 # make 'y' even by right shifting by 1
        x = (x * x) % p
    return result

def miller_rabin(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True 
    d = n - 1
    # base cases ensure 'n' is odd to make 'n - 1' even, expressing it as 'd * 2s'
    while d % 2 == 0:
        d //= 2 
        # Fermat's little theorem: 'a^n ≡ a % n' for prime 'n', if 'a' is coprime (i.e. has no common factors w/ 'n' other than 1).
    for _ in range(4):
        # from the previous points, it can be seen that for a random base 'a' in the range '[2.. n - 2]', 'a^(d * 2^r) % n' must be 1 for 'n' to be prime; more random bases improve accuracy.
        a = 2 + randint(1, n - 4) 
        x = _power(a, d, n) # computer 'a^d mod n'
        # Euclid's lemma: if prime 'n' divides the product of two numbers '(x * y)', it must divide at least one of those numbers. Thus, '(x^2 % n = 1)' or '(x % n = 1 or x % n = -1)'
        if x != 1 and x != n - 1: 
            while d != n - 1 and x != n - 1:
                x = (x * x) % n
                d *= 2
                if x == 1:
                    return False
            # from points 1 and 3, it can be seen that for 'n' to be prime, 'a^d % n = 1' or 'a^(d * 2i) % n = -1' for some 'i', where '0 <= i <= r-1'.
            if x != n - 1:
                return False
    return True
