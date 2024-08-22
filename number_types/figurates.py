def figurates(sides, limit):
    """ P(s, n) = (n * ((s - 2) * n - (s - 4))) / 2, where s and n are the 
    number of sides and index of the figurate number. This can be represented 
    by a regular geometrical arrangement of equally spaced points. """
    return [figuarate for n in range(1, limit) if (figuarate := n * ((sides - 2) * n - (sides - 4)) // 2) < limit]
