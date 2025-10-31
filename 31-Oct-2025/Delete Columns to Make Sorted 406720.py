# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for j in range(len(strs[0])):
            ans = []
            for i in range(len(strs)):
                ans.append(strs[i][j])
            if ans != sorted(ans):
                cnt += 1
        return cnt 