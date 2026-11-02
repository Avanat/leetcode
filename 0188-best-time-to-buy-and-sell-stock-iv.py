class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)

        if n < 2 or k == 0:
            return 0

        if k >= n // 2:
            return sum(
                max(0, prices[i] - prices[i - 1])
                for i in range(1, n)
            )

        dp = [0] * n

        for t in range(k):
            max_diff = -prices[0]
            curr = [0] * n

            for i in range(1, n):
                curr[i] = max(
                    curr[i - 1],
                    prices[i] + max_diff
                )

                max_diff = max(
                    max_diff,
                    dp[i] - prices[i]
                )

            dp = curr

        return dp[-1]
