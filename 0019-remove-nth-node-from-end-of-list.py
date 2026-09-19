class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        if n == length:
            return head.next

        current = head

        for _ in range(length - n - 1):
            current = current.next

        current.next = current.next.next

        return head
