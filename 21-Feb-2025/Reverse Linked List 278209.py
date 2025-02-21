# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        itr = head
        while itr :
            new_node = ListNode(itr.val,dummy.next)
            dummy.next = new_node
            itr = itr.next
        return dummy.next

            