class Solution(object):
    def permute(self, nums):
        result = [[]]

        for num in nums:
            new_result = []

            for arr in result:
                for i in range(len(arr) + 1):
                    new_arr = arr[:i] + [num] + arr[i:]
                    new_result.append(new_arr)

            result = new_result

        return result
