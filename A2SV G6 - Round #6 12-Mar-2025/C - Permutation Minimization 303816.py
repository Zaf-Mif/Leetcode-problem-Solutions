# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    deq = deque()
    temp = p[0]
    deq.append(p[0])
    for num in range(1 , len(p)):
        if deq[0] < p[num]:
            deq.append(p[num])
        elif deq[0] > p[num]:
            deq.appendleft(p[num])

    print(*deq)