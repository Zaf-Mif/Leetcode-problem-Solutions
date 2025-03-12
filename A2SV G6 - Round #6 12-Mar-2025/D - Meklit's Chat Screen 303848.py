# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n , k = map(int,input().split())
id = list(map(int,input().split()))
stack = deque()
myset = set()
for i in id :
    if i in myset:
        continue
    else:
        if len(stack) == k:
            id1 = stack.pop()
            myset.remove(id1)
        stack.appendleft(i)
        myset.add(i)

print(len(stack))
print(*stack)