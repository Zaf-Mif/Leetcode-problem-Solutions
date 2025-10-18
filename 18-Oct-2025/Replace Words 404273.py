# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        woarr = sentence.split()
        hash = set(dictionary)

        def shotest(word, hash):
            for i in range(len(word)):
                root = word[0:i]
                if root in hash:
                    return root
            return word

        for word in range(len(woarr)):
            woarr[word] = shotest(woarr[word], hash)

        return " ".join(woarr)