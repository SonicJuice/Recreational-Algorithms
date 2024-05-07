def _digit_sum(num, base):
    total = 0
    while num:
        total += num % base
        num //= base
    return total

def _int_to_base(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number > 0:
        """ repeatedly divide number by the base and append the remainders, 
        before mapping them to digits. divmod() returns a tuple containing 
        the quotient and remainder of argument1 divided by argument2. """
        number, remainder = divmod(number, base)
        result = digits[remainder] + result
    if result == "":
        result = "0"
    return result

def harshads(base, limit):
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36 inclusive")
    """ time complexity: O(limit * log(num)), where num is the maximum number < limit. """
    return [_int_to_base(i, base) for i in range(1, limit) if i % _digit_sum(i, base) == 0] # harshads are divisible by their digit sums in some base n.
