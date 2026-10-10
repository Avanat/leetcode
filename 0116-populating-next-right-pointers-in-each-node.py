
class Solution(object):
    def connect(self, root):
        if not root:
            return root

        if root.left:
            root.left.next = root.right

        if root.right and root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
