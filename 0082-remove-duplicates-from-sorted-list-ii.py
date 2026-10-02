class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            duplicate = False

            while curr.next and curr.val == curr.next.val:
                duplicate = True
                curr = curr.next

            if duplicate:
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next
