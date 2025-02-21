# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head:
            itr = head.next
            while itr:
                if prev.val == itr.val :
                    prev.next = itr.next
                    itr = itr.next
                else:
                    prev = prev.next
                    itr = itr.next
        return head
