import heapq
from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        point_building_list = [] # list of (x_pos, h, is_entering)
        for idx, b in enumerate(buildings):
            if b[2] == 0 or b[0] >= b[1]:
                continue
            point_building_list.append((b[0], b[2], 1))
            point_building_list.append((b[1], -b[2], 0))
        # entering before leaving; entering: highest first, leaving: lowest first
        point_building_list.sort(key=lambda x: (x[0],-x[1])) 
        
        cur_heights = [0] # *-1 to h, to use min_heap for finding max h 
        for (x, h, is_entering) in point_building_list:
            if is_entering:
                if h > -cur_heights[0]:
                    res.append([x, h])
                heapq.heappush(cur_heights, -h)
            else: # remember h is *-1 here
                cur_heights.remove(h)
                heapq.heapify(cur_heights)
                if h < cur_heights[0]:
                    res.append([x, -cur_heights[0]])
        return res

def mySkyline(buildings):
    sol = []
    Ps = []
    for l, r, h in buildings:
        Ps.append([l, h, True])
        Ps.append([r, h, False])
    Ps.sort(key=lambda u: [u[0], -u[1], -u[2]])
    Q = [0]
    for x, h, is_begin in Ps:
        print(Q)
        if is_begin:
            if -Q[0] < h:
                if sol and sol[-1][0] == x:
                    sol[-1] = [x, h]
                else:
                    sol.append([x, h])
            heapq.heappush(Q, -h)
        else:
            Q.remove(-h)
            heapq.heapify(Q)
            if -Q[0] < h:
                if sol and sol[-1][0] == x:
                    sol[-1] = [x, -Q[0]]
                else:
                    sol.append([x, -Q[0]])
    return sol

if __name__ == '__main__':
    a = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    b = [[1,2,1],[2,3,1]]
    print(mySkyline(b))