# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charS = Counter(chars)
        ans = 0
        for i in range(len(words)):
            cnt = Counter(words[i])
            if cnt-charS == {}:
                ans += len(words[i])
        return ans