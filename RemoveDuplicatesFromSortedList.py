"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        curr = A
        val = None
        while curr.next != None:
            val = curr.val
            if val == curr.next.val:
                nextup = curr.next
                curr.next = nextup.next
                continue
            curr = curr.next
        return A
