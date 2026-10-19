class Solution(object):
    def insertionSortList(self, head):
        values = []
        current = head

        while current:
            values.append(current.val)
            current = current.next

        values.sort()

        current = head
        for value in values:
            current.val = value
            current = current.next

        return head
