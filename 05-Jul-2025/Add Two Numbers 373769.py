# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

dummy = ListNode()
        self.current = dummy
        self.carry = 0

        def solve(list1 , list2 ):
            if not list1 and not list2 and not self.carry:
                return self.current

            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            ans = v1 + v2 + self.carry

            self.carry = ans // 10
            ans = ans % 10
                
            self.current.next = ListNode(ans)
            self.current = self.current.next

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
            # print(self.current)

            return solve(list1,list2)
        solve(l1,l2)
        return dummy.next