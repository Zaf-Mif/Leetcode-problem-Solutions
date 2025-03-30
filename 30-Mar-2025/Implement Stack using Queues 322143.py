# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

# class Node :
#     def __ init__(self , next = None , prev = None , val = 0):
        
class MyStack:
     
    def __init__(self):
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)

    def pop(self) -> int:
        ans = self.deq.pop()
        return ans

    def top(self) -> int:
        return self.deq[-1]

    def empty(self) -> bool:
        if len(self.deq) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()