'''
Problem: A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
'''

from typing import List

class Solution:
    '''
    Complexity: O(n^2) time and space (without memorization, dfs only leads to O(n^3) time, not optimal) 
    '''
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        steps = set(stones)
        impass = set()
        Q = [(stones[0], 0)]
        while Q:
            p, k = Q.pop()
            if p == stones[-1]:
                return True
            impass.add((p, k))
            if k-1 > 0 and p+k-1 in steps and (p+k-1, k-1) not in impass:
                Q.append((p+k-1, k-1))
            if k > 0 and p+k in steps and (p+k, k) not in impass:
                Q.append((p+k, k))
            if p+k+1 in steps and (p+k+1, k+1) not in impass:
                Q.append((p+k+1, k+1))
            
        return False