# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # Write your code here
    last = arr[-1]

    for i in range(len(arr)-1,-1,-1):
        if i == 0:
            arr[i] = last
            print(*arr)
            break
            
        elif arr[i-1] > last:
            arr[i] = arr[i-1]
            print(*arr)
            
        else:
            arr[i] = last
            
            print(*arr)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
