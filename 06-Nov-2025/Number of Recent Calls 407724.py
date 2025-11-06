# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.w = deque()

    def ping(self, t: int) -> int:
        self.w.append(t)     
        while self.w and self.w[0] < (t-3000):
            self.w.popleft()
        return len(self.w)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)