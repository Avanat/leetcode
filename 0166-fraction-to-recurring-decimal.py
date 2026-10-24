class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        negative = (numerator < 0) != (denominator < 0)

        numerator = abs(numerator)
        denominator = abs(denominator)

        integer = numerator // denominator
        remainder = numerator % denominator

        result = ("-" if negative else "") + str(integer)

        if remainder == 0:
            return result

        result += "."
        seen = {}

        while remainder:
            if remainder in seen:
                pos = seen[remainder]
                result = result[:pos] + "(" + result[pos:] + ")"
                break

            seen[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        return result
