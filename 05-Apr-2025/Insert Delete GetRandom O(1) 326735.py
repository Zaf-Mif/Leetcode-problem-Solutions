# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.randomized = set()        

    def insert(self, val: int) -> bool:
        if val in self.randomized :
            return False
        else:
            self.randomized.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomized :
            self.randomized.remove(val)
            return True        
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomized))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()