# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]


    def reserve(self) -> int:
        num = heapq.heappop(self.seats)
        return num
    def unreserve(self, num: int) -> None:
        heapq.heappush(self.seats, num)        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(num)