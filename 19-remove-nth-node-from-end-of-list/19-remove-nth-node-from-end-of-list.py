# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
제대로 풀이하지 못한 문제
https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164542/JS-Python-Java-C%2B%2B-or-Easy-Two-Pointer-Solution-w-Explanation
참고하여 복기하기기
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast_runner, slow_runner = head, head

        for _ in range(n):
            fast_runner = fast_runner.next

        if not fast_runner:
            return head.next

        while fast_runner.next:
                
            fast_runner,slow_runner = fast_runner.next,slow_runner.next

        slow_runner.next = slow_runner.next.next

        return head