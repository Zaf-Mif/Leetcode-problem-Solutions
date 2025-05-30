# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(" ")
        arr = [0] *( len(splitted)+1)
        for i in range(len(splitted)):
            idx = int(splitted[i][-1])
            arr[idx] = splitted[i][:-1]
        ss = ""
        for word in arr:
            if word == 0:
                continue
            else:
                ss += (word +" ")
        return ss[:-1]