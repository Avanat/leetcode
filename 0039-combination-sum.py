class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                path.append(num)
                backtrack(i, remaining - num, path)
                path.pop()

        candidates.sort()
        backtrack(0, target, [])
        return result
