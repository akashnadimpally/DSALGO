# l1 = [1,2,4]
# l2 = [1,3,4]
#
# l3 = l1+l2
#
# m = sorted(l3)
#
# print(m)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.ConvertToList(list1)
        l2 = self.ConvertToList(list2)

        c = sorted(l1 + l2)

        dummy = ListNode(0)
        curr = dummy
        for val in c:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def ConvertToList(self, listA: Optional[ListNode]) -> list:
        i = 0
        l = []
        while (listA != None):
            l.append(listA.val)
            listA = listA.next
            i += 1
        return l










