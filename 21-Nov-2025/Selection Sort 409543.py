# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        nim = 0
        while nim < n:
            for i in range(nim,n):
                if arr[nim] > arr[i]:
                    arr[nim] , arr[i] = arr[i] , arr[nim]
            nim += 1
        return arr