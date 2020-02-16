"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Try solving it using constant additional space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        circle_len = self.isCycle(A)
        if not circle_len:
            return None
        yalla = A
        for i in range(circle_len):
            yalla = yalla.next
        start = A
        while yalla != start:
            start = start.next
            yalla = yalla.next
        return yalla
        
        
    def isCycle(self, A):
        slow = A
        fast = slow.next
        while fast is not None and slow != fast:
            if not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            counter = 1
            fast = fast.next
            while fast != slow:
                fast = fast.next
                counter += 1
            return counter
