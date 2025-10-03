# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

import math

def is_square(x: int) -> bool:
    if x < 0:
        return False
    root = int(math.isqrt(x))  # Efficient integer square root
    return root * root == x

def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    s = sum(numbers)
    print("YES" if is_square(s) else "NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
