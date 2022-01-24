# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast_runner = head
        slow_runner = head
        
        reserved_node = None
        
        while fast_runner and fast_runner.next:
            fast_runner = fast_runner.next.next
            slow_runner,reserved_node,reserved_node.next = slow_runner.next , \
                                                            slow_runner, \
                                                            reserved_node
        if fast_runner:
            slow_runner = slow_runner.next
            
        while reserved_node and (slow_runner.val == reserved_node.val):
            slow_runner ,reserved_node = slow_runner.next,reserved_node.next
        
        return False if reserved_node else True
            