from typing import List

def robber(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    for i in range(2, n):
        nums[i] += max(nums[i-2], nums[i-3] if i>2 else -float('inf'))
    return max(nums[-1], nums[n-2])
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(robber(nums[:n-1]), robber(nums[1:]))