"""
Given a linked list, remove the nth node from the end of list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if not A or not A.next:
            return None
        first = A
        remove = A.next
        last = A
        for i in range(B):
            if last is None or last.next is None:
                return A.next
            last = last.next
            
        while last.next != None:
            first = first.next
            remove = remove.next
            last = last.next
        first.next = remove.next
        return A
