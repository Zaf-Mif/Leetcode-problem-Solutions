# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        temp.sort()
        dummy = ListNode(0)
        current = dummy

        for i in temp:
            current.next = ListNode(i)
            current = current.next

        return dummy.next