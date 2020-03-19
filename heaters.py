from typing import List
def abs(a):
    return a if a >= 0 else -a
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        mx = -1
        currH = 0
        n = len(heaters)
        
        for h in houses:
            while currH+1 < n:
                if abs(h-heaters[currH]) >= abs(h-heaters[currH+1]):
                    currH += 1
                else:
                    break
            if mx < abs(h-heaters[currH]):
                mx = abs(h-heaters[currH])
        return mx