class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        result = []

        factorial = 1
        for i in range(1, n):
            factorial *= i

        k -= 1

        while nums:
            index = k // factorial
            result.append(nums.pop(index))

            if not nums:
                break

            k %= factorial
            factorial //= len(nums)

        return "".join(result)
