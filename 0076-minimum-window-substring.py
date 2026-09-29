class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        required = len(t)
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            if s[right] in need:
                if need[s[right]] > 0:
                    required -= 1
                need[s[right]] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        required += 1

                left += 1

        return result
