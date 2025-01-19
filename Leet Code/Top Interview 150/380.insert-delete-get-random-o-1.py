#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.rndSet=[]

    def insert(self, val: int) -> bool:
        if self.rndSet.count(val)==0:
            self.rndSet.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.rndSet.count(val)==1:
            self.rndSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        i=random.randint(0, len(self.rndSet)-1)
        return self.rndSet[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

