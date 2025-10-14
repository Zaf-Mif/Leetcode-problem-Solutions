# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def common(self, word: str):
        cur = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if not cur.children[idx]:
                return None 
            cur = cur.children[idx]
        return cur

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if not  cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        node = self.common(word)
        return node is not None and node.is_end  

    def startsWith(self, prefix: str) -> bool:
        return self.common(prefix) is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)