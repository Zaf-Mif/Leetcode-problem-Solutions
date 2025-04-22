# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

from math import ceil
def kicks(kick , ans, firstk , secondk , i = 0):
    if i >= 10:
       return 
    
    remain = 10 - i
    if i % 2 == 0:
        if firstk + ceil(remain / 2) < secondk or secondk + (remain // 2) < firstk:
            ans[0] = min(ans[0] , i)
            return 
            
        if kick[i] == "1":
            kicks(kick ,ans, firstk+1 , secondk , i + 1)
        elif kick[i] == "0":
            kicks(kick,ans, firstk , secondk , i + 1)
        else:
            kicks(kick,ans, firstk + 1 , secondk , i + 1)
            kicks(kick,ans, firstk , secondk , i + 1)

            
    else:
        if secondk + ceil(remain / 2) < firstk or firstk +  (remain // 2) < secondk:
            ans[0] = min(ans[0] , i)
            return 
        
        if kick[i] == "1":
            kicks(kick,ans, firstk , secondk + 1 , i + 1)
        elif kick[i] == "0":
            kicks(kick,ans, firstk , secondk , i + 1)
        else:
            kicks(kick,ans, firstk , secondk + 1 , i + 1)
            kicks(kick,ans, firstk , secondk , i + 1)
            

t = int(input())
for _ in range(t):
    kick = input()
    ans = [len(kick)]
    kicks(kick , ans,0,0)
    print(ans[0])

