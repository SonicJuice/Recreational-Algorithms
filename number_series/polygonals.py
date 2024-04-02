def polygonals(sides, limit):
    polygonal_numbers = []
    n = 1
    generate = True
    while generate:
        """
        nth-s-agonal number: 'P(s, n) = (n * ((s - 2) * n - (s - 4))) /', where 's' and 'n' are the number of sides and index 
        of the polygonal number. These represent dots arranged as regular polygons (i.e. plane figures of connected line segments, 
        with equal vertex angles and side lengths)
        """
        result = (n * ((sides - 2) * n - (sides - 4))) // 2
        if result > limit + 1:
            generate = False
        else:
            polygonal_numbers.append(result)
            n += 1
    return polygonal_numbers
