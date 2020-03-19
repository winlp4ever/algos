from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0 for _ in range(num+1)]
        p = 1
        for i in range(1, num+1):
            if i >= 2*p:
                p *= 2
            res[i] = res[i-p]+1
        return res