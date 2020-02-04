from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        l = len(nums)
        mi = [0 for _ in nums]
        mn = float('inf')
        for i, n in enumerate(nums):
            mn = min(mn, n)
            mi[i] =  mn
        for j in range(l-1, -1, -1):
            if nums[j] > mi[j]:
                while stack and stack[-1] <= mi[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
            
            