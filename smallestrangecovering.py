from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        its = [iter(arr) for arr in nums]
        N = sum(list(map(lambda a: len(a), nums)))

        Q = [] # min heap
        mx = -float('inf')
        for k, it in enumerate(its):
            val = next(it)
            mx = max(mx, val)
            heapq.heappush(Q, (val, k))
        print(Q)
        mn = Q[0][0]
        dist = mx - mn
        for _ in range(1, N):
            _, i = heapq.heappop(Q)
            v = next(its[i], float('inf'))
            heapq.heappush(Q, (v, i))
            mx = max(v, mx)
            if mx - Q[0][0] < dist:
                mn = Q[0][0]
                dist = mx - mn
        return [mn, mn+dist]

if __name__ == "__main__":
    a = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    sol = Solution()
    print(sol.smallestRange(a))