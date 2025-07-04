# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff_array = [
            0
        ] * n  # Initialize a difference array with all elements set to 0

        # Process each shift operation
        for shift in shifts:
            if shift[2] == 1:  # If direction is forward (1)
                diff_array[shift[0]] += 1  # Increment at the start index
                if shift[1] + 1 < n:
                    diff_array[
                        shift[1] + 1
                    ] -= 1  # Decrement at the end+1 index
            else:  # If direction is backward (0)
                diff_array[shift[0]] -= 1  # Decrement at the start index
                if shift[1] + 1 < n:
                    diff_array[
                        shift[1] + 1
                    ] += 1  # Increment at the end+1 index

        result = list(s)
        number_of_shifts = 0

        for i in range(n):
            number_of_shifts = (
                number_of_shifts + diff_array[i]
            ) % 26  
            if number_of_shifts < 0:
                number_of_shifts += 26  
            shifted_char = chr(
                (ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a")
            )
            result[i] = shifted_char

        return "".join(result)