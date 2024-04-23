def figurates(sides, limit):
    n = 0
    generate = True
    while generate:
        """ P(s, n) = (n * ((s - 2) * n - (s - 4))) / 2, where s and n are the number 
        of sides and index of the figurate number. This can be represented by a 
        regular geometrical arrangement of equally spaced points. """
        result = (n * ((sides - 2) * n - (sides - 4))) // 2
        if result > limit + 1:
            generate = False
        else:
            """ time complexity: O(n) """
            yield result
            n += 1
