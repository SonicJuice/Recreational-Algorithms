def polygonals(sides, limit):
    result = 1
    n = 1
    while result < limit + 1:
        yield result
        """
        nth-s-agonal number: P(s, n) = ((s - 2) * n^2 - (s - 4) * n) / 2. These represent dots arranged as regular polygons 
        (plane figures of connected line segments, with equal vertex angles and side lengths)
        """
        result += (sides - 2) * n + 1
