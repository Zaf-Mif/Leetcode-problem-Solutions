# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for i in range(len(arr)):
            prefix.append(prefix[-1] ^ arr[i])

        res = []
        for left , right in queries:
            res.append(prefix[right+1] ^ prefix[left])
            
        return(res)