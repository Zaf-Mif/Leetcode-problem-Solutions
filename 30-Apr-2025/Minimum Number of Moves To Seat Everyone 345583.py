# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        def findmax(arr):
            maximum = 0
            for i in range(len(arr)):
                if arr[i] > maximum:
                    maximum = arr[i]

            return maximum

        maxposition = max(findmax(seats) , findmax(students))
        differences = [0]*maxposition

        for i in seats:
            differences[i-1] += 1
        print(differences)
        for i in students:
            differences[i-1] -= 1
        print(differences)
        
        moves = 0
        unmatched = 0
        
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference
        return moves