from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        largers = [-1 for _ in nums2]
        i = 0
        stack = []
        while i < n:
            while stack and nums2[i] > stack[-1][1]:
                u, _ = stack.pop()
                largers[u] = nums2[i]
            stack.append((i, nums2[i]))    
            i += 1
        u = {a: b for a, b in zip(nums2, largers)}
        return [u[k] for k in nums1]