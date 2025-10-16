# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode():
    def __init__(self, char):
        self.is_end = False
        self.children = [None for i in range(26)]
        self.char = char
class TrieOp:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if not  cur.children[idx]:
                cur.children[idx] = TrieNode(s)
            cur = cur.children[idx]
        cur.is_end = True

    def getAnswer(self, node):
        if not node or not node.is_end and node != self.root:
            return []
        
        ans = [[]]
        for i in range(26):
            if not node.children[i]:
                continue
            ans.append(self.getAnswer(node.children[i]))
        ans.sort(key=lambda item:(-len(item), item[-1] if len(item) > 0 else "z" ))
        ans[0].append(node.char)
        return ans[0]

class Solution:
    def longestWord(self, words: List[str]) -> str:
        sol = TrieOp()
        for word in words:
            sol.insert(word)
        return "".join(sol.getAnswer(sol.root)[::-1])