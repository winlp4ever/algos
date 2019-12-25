'''problem:
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
    
        if (target == 0) or (nums == []):
            return 0

        for i in range(len(nums)):
            if target < nums[i]:
                fk = i
                nums = nums[0:fk]
                break


        dp = [0 for i in range(target+1)]

        for i in nums:
            dp[i] = 1

        for i in range(len(dp)):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
                else:
                    break

        return dp[-1]

    '''
    if order is not taken into consideration, then the solution should be
    '''
    def orderNotCount(self, nums: List[int], target: int):
        if not nums:
            return 0
        memo = dict()
        nums.sort()
        n = len(nums)
        def rec(i, s):
            if (i, s) in memo:
                return memo[(i, s)]
            if s == 0:
                return 1
            if s < 0 or i >= n:
                return 0
            res = rec(i+1, s) + rec(i, s-nums[i])
            memo[(i, s)] = res
            return res
        res = rec(0, target)
        print(memo)
        return res
        