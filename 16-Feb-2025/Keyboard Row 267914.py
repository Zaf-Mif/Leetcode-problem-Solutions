# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        hash = {}
        result = []
        for i in range(len(res)):
            for j in res[i]:
                hash[j] = i + 1
        print(hash)
        for word in words:
            prev = 0 
            valid = True
            saved = word
            word = word.lower()

            for letter in word:
                if prev == 0:
                    prev = hash[letter]
                else:
                    if prev!= hash[letter]:
                        valid = False
                        break
            if valid:
                result.append(saved)
        
        return result
            