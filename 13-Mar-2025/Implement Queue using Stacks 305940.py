# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        self.front_stack.append(x)
        self.back_stack = self.front_stack[::-1]

    def pop(self) -> int:
        ans = self.back_stack.pop()
        self.front_stack = self.back_stack[::-1]
        return ans
        
    def peek(self) -> int:
        return self.back_stack[-1]

    def empty(self) -> bool:
       return not self.back_stack



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()