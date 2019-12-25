from typing import List

from heapq import *
class Solution:
    def kthSmallest(self, lists: List[List[int]], k: int) -> int:
        minHeap, count = [], 0
        for i in range(len(lists)):
            if len(lists[i]) >= 1:
                heappush(minHeap, (lists[i][0], 0, lists[i]))
        while minHeap and count <= k:
            ele, index, lst = heappop(minHeap)
            if index+1 < len(lst):
                heappush(minHeap, (lst[index+1], index+1, lst))
            count += 1
            if count == k:
                return ele

    def sol_2(self, lists, k):
        _1dlist = []
        for l in lists:
            for e in l:
                _1dlist.append(e)
        return sorted(_1dlist)[k-1]