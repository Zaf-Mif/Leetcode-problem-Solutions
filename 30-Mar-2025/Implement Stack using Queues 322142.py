# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

# class Node :
#     def __ init__(self , next = None , prev = None , val = 0):
        
class MyStack:
     
    def __init__(self):
        self.first_queue = deque()
        self.second_queue = deque()

    def push(self, x: int) -> None:
        self.first_queue.append(x)
        self.second_queue = deque(reversed(self.first_queue))
        

    def pop(self) -> int:
        ans = self.second_queue.popleft()
        self.first_queue = deque(reversed(self.second_queue))
        return ans

    def top(self) -> int:
        return self.second_queue[0]

    def empty(self) -> bool:
        return len(self.second_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()