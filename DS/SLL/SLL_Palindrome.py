# l = ['1','2','2','1']
# k = []
# m = ''.join(l)
#
# print(m)
#
# n = len(l)
# for i in range(n-1,-1,-1):
#     k.append(l[i])
#
# h = ''.join(k)
#
# print(h)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        i = 0
        while (head != None):
            l.append(str(head.val))
            head = head.next
            i += 1

        k = []
        m = ''.join(l)
        n = len(l)
        for i in range(n - 1, -1, -1):
            k.append(l[i])

        h = ''.join(k)

        if (m == h):
            return True
        else:
            return False