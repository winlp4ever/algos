from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        mxs = []
        n = len(nums)
        Q = deque()
        for i in range(k):
            while Q and nums[i] >= nums[Q[-1]]:
                Q.pop()
            Q.append(i)
        mxs.append(nums[Q[0]])

        for i in range(k, n):
            while Q and Q[0] <= i-k:
                Q.popleft()
            while Q and nums[Q[-1]] <= nums[i]:
                Q.pop()
            Q.append(i)
            mxs.append(nums[Q[0]])
        return mxs