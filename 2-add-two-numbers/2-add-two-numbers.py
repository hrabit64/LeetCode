# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        reserved_l = None
        round = 0
        while l1 or l2 or round:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            if not reserved_l:
                reserved_l = ListNode(val=((sum + round )% 10), next=None)

            else:
                idx = reserved_l
                while idx.next:
                    idx = idx.next
                node = ListNode(val=((sum + round)% 10), next=None)
                idx.next = node

            round = (sum+round) // 10

        return reserved_l