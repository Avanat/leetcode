class Solution(object):
    def combine(self, n, k):
        result = []

        def backtrack(start, current):
            if len(current) == k:
                result.append(current)
                return

            for i in range(start, n + 1):
                backtrack(i + 1, current + [i])

        backtrack(1, [])
        return result
