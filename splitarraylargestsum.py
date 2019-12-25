'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)

        def no_of_partitions(nums,max_sum):
            curr_sum=0
            partitions=1
            for i in range(len(nums)):
                if(curr_sum+nums[i]<=max_sum):
                    curr_sum+=nums[i]
                else:
                    curr_sum = nums[i]
                    partitions+=1
            return partitions

        while l<r:
            mid = l + (r-l)//2
            if(no_of_partitions(nums,mid)>m):
                l=mid+1
            else:
                r=mid

        ans=l

        for i in range(l,r+1):
            if(no_of_partitions(nums,i)==m):
                ans=i
                break
        return ans