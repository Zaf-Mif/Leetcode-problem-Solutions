class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        1. max: remap first non 9 digit to 9 (if any)
        2. min: remap first non 0 to 0 (if any)
        """
        num_max = []
        num_min = []
        frm9 = frm0 = -1
        for c in str(num):
            if frm9 == -1 and c != '9':
                frm9 = c
            if frm0 == -1 and c != '0':
                frm0 = c
            num_max.append('9' if c == frm9 else c)
            num_min.append('0' if c == frm0 else c)
        return int(''.join(num_max)) - int(''.join(num_min))