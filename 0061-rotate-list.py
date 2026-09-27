class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        k %= len(nodes)

        if k == 0:
            return head

        new_head = nodes[-k]
        nodes[-k - 1].next = None

        current = new_head
        while current.next:
            current = current.next

        current.next = head
        return new_head
