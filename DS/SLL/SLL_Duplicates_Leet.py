# l = [-1,0,0,0,0,3,3]
#
# t = set(l)
# res = list(t)
#
# print(t)
# print(res)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        l = []
        i = 0
        while (head != None):
            l.append(head.val)
            head = head.next
            i += 1

        t = set(l)

        res = sorted(list(t))

        dummy = ListNode(0)
        curr = dummy
        for val in res:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next