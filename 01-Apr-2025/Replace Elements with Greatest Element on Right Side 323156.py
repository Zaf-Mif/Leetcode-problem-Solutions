# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        largest = -1
        for i in range(len(arr)-1 , -1 , -1):
            ans.append(largest)

            largest = max(arr[i], largest)

        return ans[::-1]