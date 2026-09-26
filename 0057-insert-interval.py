class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()

        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval[:])
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
