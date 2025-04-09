# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

def socialism(arr):
    arr.sort()
    arr = "".join(arr)
    return arr

t  = int(input())
for _ in range(t):
    s = input()
    print(socialism(list(s)))