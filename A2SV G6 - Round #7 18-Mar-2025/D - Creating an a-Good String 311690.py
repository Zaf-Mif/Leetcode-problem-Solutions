# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D


def solution():
    n = int(input())
    s = input()
    
    def findNumberOfOperations(left, right, char):
        if left == right:
            if s[left] == char:
                return 0
            return 1
        
        mid = (left+right)//2
        right_half = (right-mid) - s.count(char, mid+1, right+1)
        total_first = findNumberOfOperations(left, mid, chr(ord(char)+1)) + right_half
        
        
        left_half = (mid-left+1) - s.count(char, left, mid+1)
        total_second = findNumberOfOperations(mid+1, right, chr(ord(char)+1)) + left_half
        
        return min(total_first, total_second)
    
    return findNumberOfOperations(0, n-1, 'a')
        
        
        

t = int(input())
for _ in range(t):
    print(solution())