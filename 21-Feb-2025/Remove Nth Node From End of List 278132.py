# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 1
        itr = head
        while itr and itr.next:
            itr = itr.next
            cnt += 1
        index = cnt - n

        dummy = ListNode()
        dummy.next = head

        prev = dummy
        count = 0
    
        while prev.next and count < index:
            prev = prev.next
            count += 1

        if prev.next and count == index:
            prev.next = prev.next.next
        
        return dummy.next