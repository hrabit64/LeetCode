# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow = head,head
        
        while fast:
            if not fast.next:
                break
            
            slow,fast = slow.next,fast.next.next
        
        return slow
        