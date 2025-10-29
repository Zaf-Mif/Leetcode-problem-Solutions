# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        vowel = 'aeiou'
        for i in range(n):
            if word[i] in vowel:
                ans += ((i+1) * (n-i))
        return ans 
