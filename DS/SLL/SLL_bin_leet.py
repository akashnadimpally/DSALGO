# head = [1,0,1]
#
# l = [str(i) for i in head]
#
# print(l)
#
# k = ''.join(l)
#
# print(k)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while(head != None):
            l.append(str(head.val))
            head = head.next
        m = ''.join(l)
        k = int(m,2)
        return k
