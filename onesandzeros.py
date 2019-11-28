'''Link:

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
'''
import collections 
from typing import List

class Solution:
    '''
    Idea dynamic programming, this is in fact a version of knapsack problem
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = collections.defaultdict(int)
        for string in strs:
            ones = string.count("1")
            counts[ones, len(string) - ones] += 1
        nums = list(counts.keys())
        def dfs(idx, m, n):
            if idx == len(nums): return 0
            if (idx, m, n) in d: return d[idx, m, n]
            ones, zeros = nums[idx]
            tmp = counts[ones, zeros]
            if ones > 0:
                tmp = min(tmp, n // ones)
            if zeros > 0:
                tmp = min(tmp, m // zeros)
            ans = 0
            for i in range(tmp + 1):
                val = i + dfs(idx + 1, m - i * zeros, n - i * ones)
                ans = max(ans, val)
            d[idx, m, n] = ans
            return ans
        d = {}
        return dfs(0, m, n)