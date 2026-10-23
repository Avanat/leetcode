class Solution(object):
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        low, high = min(nums), max(nums)

        if low == high:
            return 0

        size = max(1, (high - low + n - 2) // (n - 1))
        count = (high - low) // size + 1

        bucket_min = [float('inf')] * count
        bucket_max = [float('-inf')] * count
        used = [False] * count

        for num in nums:
            i = (num - low) // size
            bucket_min[i] = min(bucket_min[i], num)
            bucket_max[i] = max(bucket_max[i], num)
            used[i] = True

        ans = 0
        prev = low

        for i in range(count):
            if used[i]:
                ans = max(ans, bucket_min[i] - prev)
                prev = bucket_max[i]

        return ans
