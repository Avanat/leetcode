class Solution:
    def isNumber(self, s):
        if not s:
            return False

        if s[0] in "+-":
            s = s[1:]

        if not s:
            return False

        if "e" in s or "E" in s:
            parts = s.replace("E", "e").split("e")

            if len(parts) != 2:
                return False

            if not parts[0] or not parts[1]:
                return False

            s = parts[0]
            exponent = parts[1]

            if exponent[0] in "+-":
                exponent = exponent[1:]

            if not exponent.isdigit():
                return False

        if s.count(".") > 1:
            return False

        s = s.replace(".", "")

        return s.isdigit()
