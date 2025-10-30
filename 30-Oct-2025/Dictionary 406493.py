# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

t = int(input())
for _ in range(t):
    s = input()
    if s[0] == "a":
        print(((ord(s[0]) - ord("a"))* 25) + (ord(s[1]) - ord("a")))
    else:
        # print((((ord(s[0]) - ord("a")) * 25) + (ord(s[1]) - ord("a")))+ 1)
        ans = (((ord(s[0]) - ord("a")) * 25) + (((ord(s[1]) - ord("a")) + 1 )) )
        if ord(s[1]) > ord(s[0]):
            ans -= 1
        print(ans)
