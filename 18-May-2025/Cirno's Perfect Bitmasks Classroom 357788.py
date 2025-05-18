# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    num = cnt = one = mark =  0
    for i in range(32):    
        if x & (1 << i) != 0 and not cnt:
            num |= (1 << i)
            mark = i 
            cnt = 1
        elif x & (1 << i) != 0:
            one = 1
    
    for i in range(32):
        if i != mark and (x & (1 << i)) == 0 and not one:
            num |= (1 << i)
            break
    print(num) 
    