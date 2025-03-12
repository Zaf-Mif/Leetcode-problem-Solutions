# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find(n,k):
            if n == 1:
                return "0"
        
            ans = find(n-1,k)
            arr = []
            for num in ans:
                if num == '0': arr.append("1")
                else: arr.append("0")

            arr = "".join(arr)    
            si = ans +"1" + arr[::-1]
            return si
            
        si = find(n,k)
        return si[k-1]
