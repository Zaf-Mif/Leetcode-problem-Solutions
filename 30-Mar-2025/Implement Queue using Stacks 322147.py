# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.fstack = []

    def push(self, x: int) -> None:
        self.fstack.append(x)

    def pop(self) -> int:
        ans = self.fstack.pop(0)
        return ans
    def peek(self) -> int:
        return self.fstack[0]

    def empty(self) -> bool:
        if len(self.fstack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()