class Solution(object):
    def maximalRectangle(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0

        for i in range(rows):
            heights = [0] * cols

            for j in range(i, rows):
                for k in range(cols):
                    if matrix[j][k] == "1":
                        heights[k] += 1
                    else:
                        heights[k] = 0

                stack = []
                heights.append(0)

                for k in range(cols + 1):
                    while stack and heights[stack[-1]] > heights[k]:
                        h = heights[stack.pop()]
                        width = k if not stack else k - stack[-1] - 1
                        max_area = max(max_area, h * width)

                    stack.append(k)

                heights.pop()

        return max_area
