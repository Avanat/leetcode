import heapq

class Solution(object):
    def getSkyline(self, buildings):
        events = sorted(set(
            [b[0] for b in buildings] + [b[1] for b in buildings]
        ))

        buildings.sort()
        heap = []
        result = []
        i = 0

        for x in events:
            while i < len(buildings) and buildings[i][0] <= x:
                l, r, h = buildings[i]
                heapq.heappush(heap, (-h, r))
                i += 1

            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            height = -heap[0][0] if heap else 0

            if not result or result[-1][1] != height:
                result.append([x, height])

        return result
