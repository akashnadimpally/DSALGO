# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        l = []
        while (head != None):
            l.append(head.val)
            head = head.next
            i+=1

        if i%2==0:
            m = i//2
            g = l[m:]
        else:
            m = i//2
            g = l[m:]

        dummy = ListNode(0)
        curr = dummy
        for val in g:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


# Error
# #         TypeError: [3, 4, 5] is not valid
# #         value
# #         for the expected return type ListNode
# #         raise TypeError(str(ret) + " is not valid value for the expected return type ListNode");
# #
# #     Line
# #     49 in _driver(Solution.py)
# #     _driver()
# #
# #
# # Line
# # 56 in < module > (Solution.py)
# # During
# # handling
# # of
# # the
# # above
# # exception, another
# # exception
# # occurred:
# # TypeError: unhashable
# # type: 'list'
# # Line
# # 40 in has_cycle(. / python3 / listnode.py)
# # Line
# # 53 in serialize(. / python3 / listnode.py)
# # Line
# # 73 in _serialize(. / python3 / __serializer__.py)
# # out = ser._serialize(ret, 'ListNode')
# # Line
# # 47 in _driver(Solution.py)

        # # Hare and Tortoise Algorithm
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow