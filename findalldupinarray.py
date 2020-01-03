'''
Problem link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''

from typing import List 

class Solution:
    '''
    complexity: O(n) time and no extra space
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sol = []
        n = len(nums)
        for i in range(1,n+1):
            if nums[i-1] < 0:
                continue
            a = nums[i-1]
            nums[i-1] = 0
            while a > 0:
                if nums[a-1] < 0:
                    sol.append(a)
                    break
                if nums[a-1] == 0:
                    nums[a-1] = -a
                    break
                    
                tmp = nums[a-1]
                nums[a-1] = -a
                a = tmp
        
                
        return sol