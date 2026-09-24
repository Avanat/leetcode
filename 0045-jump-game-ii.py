class Solution(object):
    def jump(self, nums):
        n = len(nums)
        memo = [-1] * n

        def solve(i):
            if i >= n - 1:
                return 0

            if memo[i] != -1:
                return memo[i]

            ans = float("inf")

            for j in range(1, nums[i] + 1):
                if i + j < n:
                    ans = min(ans, 1 + solve(i + j))

            memo[i] = ans
            return ans

        return solve(0)
