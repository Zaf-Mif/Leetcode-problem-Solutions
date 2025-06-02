# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    mx = max(arr)
    res = [0]*(100)
    for num in arr:
        res[num] += 1
    return res