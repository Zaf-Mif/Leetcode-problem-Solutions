# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            idx = ord(s) - ord('a')
            if not  cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True        

    def search(self, word: str) -> bool:
        def dfs(j: int, node: TrieNode) -> bool:
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if not cur.children[idx]:
                        return False
                    cur = cur.children[idx]
            return cur.is_end  
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)