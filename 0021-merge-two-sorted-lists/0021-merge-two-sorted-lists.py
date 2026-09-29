class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2

        new_head = ListNode(0)
        current = new_head

        while p1 is not None and p2 is not None:

            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next

            current = current.next

        if p1 is not None:
            current.next = p1
        else:
            current.next = p2

        return new_head.next