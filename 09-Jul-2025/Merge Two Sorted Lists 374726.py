# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution: def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: dummy = ListNode() cur = dummy while list1 and list2: if list1.val > list2.val: cur.next = list2 list2 = list2.next else: cur.next = list1 list1 = list1.next