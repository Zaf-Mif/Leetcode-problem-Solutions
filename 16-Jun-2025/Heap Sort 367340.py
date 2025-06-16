# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    def heapSort(self, arr):
        n = len(arr)

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
            heapify(arr, i, 0)

        return arr
