class Solution(object):
    def removeDuplicates(self, nums):
        unique = list(set(nums))
        unique.sort()

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)
