# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
v = list(map(int, input().split()))# costs of the stone
prefix_v = [0]

sorted_v  = sorted(v)
u = [0]# sorted- prefix_v

# prefix for v
for i in range(len(v)):
    prefix_v .append(prefix_v[-1] + v[i])
    
# prefix for sorted v
for i in range(len(v)):
    u.append(u[-1] + sorted_v[i])
    
m = int(input())

for _ in range(m):
    type , l , r = map(int, input().split())
    
    if type == 1:
        print(prefix_v[r] - (prefix_v[l-1]))
    else:
        print(u[r] - u[l-1])
        