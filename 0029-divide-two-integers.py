class Solution(object):
    def divide(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp += temp
                multiple += multiple

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        result = max(-2147483648, min(2147483647, result))

        return result
