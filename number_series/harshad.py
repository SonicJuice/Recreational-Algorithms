

class Harshad:
    def __init__(self, base):
        self.base = base

    def _digit_sum(self, num):
        total = 0
        while num:
            total += num % self.base
            num //= self.base
        return total

    def _int_to_base(self, number):
        """
        represent a positive decimal integer in a 2-36 base.
        """
        if self.base < 2 or self.base > 36:
            raise ValueError("Base must be between 2 and 36 inclusive")
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        if number < 0:
            raise ValueError("number must be a positive integer")
        while number > 0:
            """
            repeatedly divide number by the base and append the remainders, 
            before mapping them to digits 
            """
            number, remainder = divmod(number, self.base)
            result = digits[remainder] + result
        if result == "":
            result = "0"
        return result

    def harshad_numbers(self, limit):
        if self.base < 2 or self.base > 36:
            raise ValueError("Base must be between 2 and 36 inclusive")
        harshad_numbers = []
        for i in range(1, limit + 1):
            if i % self._digit_sum(i) == 0: # harshads are divisible by their digit sums in some base n.
                harshad_numbers.append(self._int_to_base(i))
        """
        time complexity: 'O(limit * log(num))', where num is the maximum number from 1 to limit (inclusive).
        """
        return harshad_numbers
