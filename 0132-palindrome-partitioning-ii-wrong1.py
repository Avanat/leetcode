
class Solution:
    def minCut(self, s):
        n = len(s)
        dp = [i for i in range(n)]

        for i in range(n):
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                dp[right] = min(dp[right], dp[left - 1] + 1 if left > 0 else 0)
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                dp[right] = min(dp[right], dp[left - 1] + 1 if left > 0 else 0)
                left -= 1
                right += 1

        return dp[n - 1]
