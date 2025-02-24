# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=left = head
        num_indecies = 1

        while current:
            if current.next: print(current.next.val, left.val)
            to_pass = 0
            while to_pass < num_indecies and current:
                current = current.next
                to_pass += 1
            if to_pass == num_indecies and current and current.next:
                next = left.next
                left.next = current.next
                var = left.next.next
                left.next.next = next
                current.next = var
                left = left.next
                current = left
            num_indecies += 1
        return head