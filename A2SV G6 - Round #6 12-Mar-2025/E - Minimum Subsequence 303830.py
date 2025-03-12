# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    zero_stack = []
    one_stack = []
    count = 0
    ans = []
    
    for i in range(len(s)):
        if s[i] == '0':
            if one_stack :
                id = one_stack.pop()
                ans.append(id)
                zero_stack.append(id)
            else:
                count += 1
                ans.append(count)
                zero_stack.append(count)
        else:
            if zero_stack:
                id = zero_stack.pop()
                ans.append(id)
                one_stack.append(id)
            else:
                count += 1
                ans.append(count)
                one_stack.append(count)
    print(count)
    print(*ans)