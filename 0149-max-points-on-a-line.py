class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        n = len(points)
        if n <= 2:
            return n

        result = 0

        for i in range(n):
            slopes = {}
            duplicates = 0
            best = 0
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                divisor = gcd(dx, dy)
                dx //= divisor
                dy //= divisor

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                elif dx < 0:
                    dx = -dx
                    dy = -dy

                slope = (dx, dy)
                slopes[slope] = slopes.get(slope, 0) + 1
                best = max(best, slopes[slope])

            result = max(result, best + duplicates + 1)

        return result
