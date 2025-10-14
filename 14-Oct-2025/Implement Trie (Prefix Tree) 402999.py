# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if not  cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        if cur.is_end:
            return True 
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            idx = ord(s) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)