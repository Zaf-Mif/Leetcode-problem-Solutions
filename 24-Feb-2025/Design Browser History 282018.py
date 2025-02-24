# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self, val = None, next = None, prev = None):
        self.val= val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.home_page = self.head

    def visit(self, url: str) -> None:
        new_history = Node(url)
        self.home_page.next = new_history
        new_history.prev =self.home_page
        self.home_page = self.home_page.next


    def back(self, steps: int) -> str:
        while steps and self.home_page.prev:
            self.home_page = self.home_page.prev
            steps -= 1
        return self.home_page.val

    def forward(self, steps: int) -> str:
        while steps and self.home_page.next:
            self.home_page = self.home_page.next
            steps -= 1
        return self.home_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)