class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        def leftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def exists(index, height, node):
            left, right = 0, (1 << height) - 1

            for _ in range(height):
                mid = (left + right) // 2

                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1

            return node is not None

        height = leftHeight(root) - 1

        if height == 0:
            return 1

        left, right = 0, (1 << height) - 1

        while left <= right:
            mid = (left + right) // 2

            if exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1

        return (1 << height) - 1 + left
