# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(" ")
        arr = [0] *( len(splitted)+1)
        for i in range(len(splitted)):
            idx = int(splitted[i][-1])
            arr[idx] = splitted[i][:-1]
        arr.remove(0)
        return " ".join(arr)