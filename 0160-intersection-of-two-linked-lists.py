class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p, q = headA, headB

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA

        return p
