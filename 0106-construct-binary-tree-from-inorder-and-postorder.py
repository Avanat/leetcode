class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        index_map = {value: i for i, value in enumerate(inorder)}

        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None

            root_value = postorder[post_end]
            root = TreeNode(root_value)

            index = index_map[root_value]
            left_size = index - in_start

            root.left = build(
                in_start,
                index - 1,
                post_start,
                post_start + left_size - 1
            )

            root.right = build(
                index + 1,
                in_end,
                post_start + left_size,
                post_end - 1
            )

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
