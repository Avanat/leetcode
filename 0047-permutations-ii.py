class Solution(object):
    def permuteUnique(self, nums):
        result = []

        def backtrack(arr, remaining):
            if not remaining:
                if arr not in result:
                    result.append(arr[:])
                return

            for i in range(len(remaining)):
                backtrack(
                    arr + [remaining[i]],
                    remaining[:i] + remaining[i + 1:]
                )

        backtrack([], nums)
        return result
